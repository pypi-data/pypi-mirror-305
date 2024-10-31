from concurrent.futures import ProcessPoolExecutor
from typing import Any, Callable, Dict, Generator, List, Tuple, Union

import openai

from burr.core import Action, Application, ApplicationBuilder, Condition, State, action
from burr.core.application import ApplicationContext
from burr.core.graph import GraphBuilder
from burr.core.parallelism import MapStates, RunnableGraph


# full agent
def _query_llm(prompt: str) -> str:
    """Simple wrapper around the OpenAI API."""
    client = openai.Client()
    return (
        client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
        )
        .choices[0]
        .message.content
    )


@action(
    reads=["feedback", "current_draft", "poem_type", "prompt"],
    writes=["current_draft", "draft_history", "num_drafts"],
)
def write(state: State) -> Tuple[dict, State]:
    """Writes a draft of a poem."""
    poem_subject = state["prompt"]
    poem_type = state["poem_type"]
    current_draft = state.get("current_draft")
    feedback = state.get("feedback")

    parts = [
        f'You are an AI poet. Create a {poem_type} poem on the following subject: "{poem_subject}". '
        "It is absolutely imperative that you respond with only the poem and no other text."
    ]

    if current_draft:
        parts.append(f'Here is the current draft of the poem: "{current_draft}".')

    if feedback:
        parts.append(f'Please incorporate the following feedback: "{feedback}".')

    parts.append(
        f"Ensure the poem is creative, adheres to the style of a {poem_type}, and improves upon the previous draft."
    )

    prompt = "\n".join(parts)

    draft = _query_llm(prompt)

    return {"draft": draft}, state.update(
        current_draft=draft,
        draft_history=state.get("draft_history", []) + [draft],
    ).increment(num_drafts=1)


@action(reads=["current_draft", "poem_type", "prompt"], writes=["feedback"])
def edit(state: State) -> Tuple[dict, State]:
    """Edits a draft of a poem, providing feedback"""
    poem_subject = state["prompt"]
    poem_type = state["poem_type"]
    current_draft = state["current_draft"]

    prompt = f"""
    You are an AI poetry critic. Review the following {poem_type} poem based on the subject: "{poem_subject}".
    Here is the current draft of the poem: "{current_draft}".
    Provide detailed feedback to improve the poem. If the poem is already excellent and needs no changes, simply respond with an empty string.
    """

    feedback = _query_llm(prompt)

    return {"feedback": feedback}, state.update(feedback=feedback)


@action(reads=["current_draft"], writes=["final_draft"])
def final_draft(state: State) -> Tuple[dict, State]:
    return {"final_draft": state["current_draft"]}, state.update(final_draft=state["current_draft"])


#
#
# def _create_sub_application(
#     max_num_drafts: int,
#     spawning_application_context: ApplicationContext,
#     poem_type: str,
#     prompt: str,
# ) -> Application:
#     """Utility to create sub-application -- note"""
#     out = (
#         ApplicationBuilder()
#         .with_actions(
#             edit,
#             write,
#             final_draft,
#         )
#         .with_transitions(
#             ("write", "edit", Condition.expr(f"num_drafts < {max_num_drafts}")),
#             ("write", "final_draft"),
#             ("edit", "final_draft", Condition.expr("len(feedback) == 0")),
#             ("edit", "write"),
#         )
#         .with_tracker(spawning_application_context.tracker.copy())  # remember to do `copy()` here!
#         .with_spawning_parent(
#             spawning_application_context.app_id,
#             spawning_application_context.sequence_id,
#             spawning_application_context.partition_key,
#         )
#         .with_entrypoint("write")
#         .with_state(
#             current_draft=None,
#             poem_type=poem_type,
#             prompt=prompt,
#             feedback=None,
#         )
#         .build()
#     )
#     return out

sub_application_graph = (
    GraphBuilder()
    .with_actions(
        edit,
        write,
        final_draft,
    )
    .with_transitions(
        ("write", "edit", Condition.expr("num_drafts < max_num_drafts")),
        ("write", "final_draft"),
        ("edit", "final_draft", Condition.expr("len(feedback) == 0")),
        ("edit", "write"),
    )
    .build()
)


# full agent
@action(
    reads=[],
    writes=[
        "max_drafts",
        "poem_types",
        "poem_subject",
    ],
)
def user_input(
    state: State, max_drafts: int, poem_types: List[str], poem_subject: str
) -> Tuple[dict, State]:
    """Collects user input for the poem generation process."""
    return {
        "max_drafts": max_drafts,
        "poem_types": poem_types,
        "poem_subject": poem_subject,
    }, state.update(max_drafts=max_drafts, poem_types=poem_types, poem_subject=poem_subject)


class GenerateAllPoems(MapStates):
    def states(
        self, state: State, context: ApplicationContext, inputs: Dict[str, Any]
    ) -> Generator[State, None, None]:
        for poem_type in state["poem_types"]:
            yield state.update(poem_type=poem_type, prompt=state["poem_subject"], max_num_drafts=2)

    def action(
        self, state: State, inputs: Dict[str, Any]
    ) -> Union[Action, Callable, RunnableGraph]:
        return RunnableGraph(sub_application_graph, entrypoint="write", halt_after=["final_draft"])

    def reduce(self, state: State, results: Generator[State, None, None]) -> State:
        new_state = state
        for output_state in results:
            new_state = new_state.append(proposals=output_state["final_draft"])
        return new_state

    @property
    def writes(self) -> list[str]:
        return ["proposals"]

    @property
    def reads(self) -> list[str]:
        return ["max_drafts", "poem_types", "poem_subject"]


@action(reads=["proposals", "prompts"], writes=["final_results"])
def final_results(state: State) -> Tuple[dict, State]:
    # joins them into a string
    proposals = state["proposals"]
    final_results = "\n\n".join(
        [f"{poem_type}:\n{proposal}" for poem_type, proposal in zip(state["poem_types"], proposals)]
    )
    return {"final_results": final_results}, state.update(final_results=final_results)


def application() -> Application:
    return (
        ApplicationBuilder()
        .with_actions(user_input, final_results, generate_all_poems=GenerateAllPoems())
        .with_transitions(
            ("user_input", "generate_all_poems"),
            ("generate_all_poems", "final_results"),
        )
        .with_tracker(project="demo:parallelism_poem_generation")
        .with_entrypoint("user_input")
        .with_parallel_executor(ProcessPoolExecutor(max_workers=-1))
        .build()
    )


if __name__ == "__main__":
    app = application()
    app.visualize(output_file_path="statemachine", format="png")
    app.run(
        halt_after=["final_results"],
        inputs={
            "max_drafts": 2,
            "poem_types": [
                "sonnet",
                "limerick",
                "haiku",
                "acrostic",
            ],
            "poem_subject": "state machines",
        },
    )
