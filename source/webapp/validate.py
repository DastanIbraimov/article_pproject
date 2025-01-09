def article_validate(article):
    errors = {}
    if not article.title:
        errors["title"] = "Title is required"
    elif len(article.title) > 50:
        errors["title"] = "Title must be less than 50 characters"

    if not article.content:
        errors["content"] = "Content is required"

    if not article.author:
        errors["author"] = "Author is required"

    return errors
