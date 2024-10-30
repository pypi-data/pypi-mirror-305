import httpx
import pyperclip


class Category:
    def __init__(self, link):
        self.categories = httpx.get(link).json()
        self.desc = self.categories.get("desc", "")

    def _repr_markdown_(self):
        keys = self.categories.keys() - {"desc"}

        return "\n".join(f"- {k} ({self.categories[k]['desc']})" for k in keys)

    def __getattr__(self, key):
        if key in self.categories:
            value = self.categories.get(key)
            if value.get("type") == "cat":
                return Category(value.get("link"))
            elif value.get("type") == "code":
                value.setdefault("title", key)
                return Code(value)
        return "Err😵"

    def __repr__(self) -> str:
        return self._repr_markdown_()


class Code:
    def __init__(self, obj: dict):
        self.title = obj.get("title", "")
        self.desc = obj.get("desc", "")
        self.code = obj.get("code", "")
        if link := obj.get("link", ""):
            self.code = httpx.get(link).text

    def __call__(self):
        self.copy()

    def copy(self):
        pyperclip.copy(self.code)

    def __repr__(self):
        return ""


def main():
    c = Category("https://pastebin.com/raw/tV6FpKL3")
    print(c.num_methods.matmul_naive())


if __name__ == "__main__":
    main()
