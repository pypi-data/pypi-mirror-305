# ESBMC-AI Addon Template

Template for creating ESBMC-AI addons.

## Setup

Simply build the package and install it to your environment. Then in ESBMC-AI's
config file add the module to load. In this case the following field will be
needed:

```toml
addon_modules = ["esbmc_ai_addon_template"]
```

Make sure that the ChatCommand is exposed using __all__ in the __init__.py file.
