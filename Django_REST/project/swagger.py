from typing import List

from drf_spectacular.openapi import AutoSchema


class MyAutoSchema(AutoSchema):

    def get_tags(self) -> List[str]:
        if "comments" in self.path:
            return ["comments"]
        if "posts" in self.path:
            return ["posts"]
        if "auth" in self.path or "token" in self.path:
            return ["auth"]
        return ["other"]
