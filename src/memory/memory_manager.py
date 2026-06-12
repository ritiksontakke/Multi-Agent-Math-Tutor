from src.memory.store import store

NAMESPACE = ("chat_memory",)

def save_message(user_id: str, role: str, content: str):
    store.put(
        NAMESPACE,
        f"{user_id}_{role}_{hash(content)}",
        {
            "user_id": user_id,
            "role": role,
            "content": content,
        }
    )

def get_history(user_id: str):
    memories = store.search(NAMESPACE)

    history = []

    for m in memories:
        if m.value["user_id"] == user_id:
            history.append(
                {
                    "role": m.value["role"],
                    "content": m.value["content"]
                }
            )

    return history