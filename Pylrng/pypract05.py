#!/usr/bin/env python3

#Logic if/elif/else

import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Development environment")
elif current_env == STAGING:
    print("Development environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Coddespace or local environment")
else:
    print("Unknown environment")
