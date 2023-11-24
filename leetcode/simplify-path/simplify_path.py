class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ''

        components = path.split('/')
        stack: list[str] = []

        for component in components:
            if component == '..':
                if stack:
                    stack.pop()
            elif component and component != '.':
                stack.append(component)

        simplified_path = '/' + '/'.join(stack)
        return simplified_path
