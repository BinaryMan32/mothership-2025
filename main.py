from mkdocs_macros.plugin import MacrosPlugin


def find_module_posts_iterate(post, iterate):
    module = post.meta['module']
    posts = []
    post = iterate(post)
    while post:
        if post.meta['module'] == module:
            posts.append(post)
        post = iterate(post)
    return posts


def define_env(env: MacrosPlugin):
    """
    This is the hook for the variables, macros and filters.
    """

    @env.macro
    def module_posts(page):
        """
        Finds all of the posts in this module.
        """
        before = find_module_posts_iterate(page, lambda p: p.previous_page)
        after = find_module_posts_iterate(page, lambda p: p.next_page)
        return before[::-1] + [page] + after
