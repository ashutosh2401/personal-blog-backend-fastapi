def blogEntity(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "author": blog["author"],
        "content": blog["content"],
        "niche": blog["niche"]
    }

def blogsEntity(blogs) -> list:
    return [blogEntity(blog) for blog in blogs]

def serializeDict(a) -> dict:
	return {**{i:str(a[i]) for i in a if i=="_id"},**{i:a[i] for i in a if i!="_id"}}

def serializeList(entity) -> list:
	return [serializeDict(a) for a in entity]
