# LitePolis Router Example

This repository provides a practical guide to creating router modules for LitePolis, expanding upon the [LitePolis-router Template](https://github.com/NewJerseyStyle/LitePolis-router-template). Think of this as a blog post-style walkthrough, demonstrating with a basic yet functional example in `core.py` how you can adapt the template and build your own LitePolis router module.

> :warning: Remember to keep the prefix "litepolis-router-" and "litepolis_router_" in your package and directory names. This naming convention is crucial for the LitePolis package manager to correctly identify and deploy your module.

This example is designed to be hands-on and educational, showcasing:

* **Basic Router Setup**: Learn how to define API routes using FastAPI's powerful `APIRouter`.  This is the foundation of your module's API.
* **Configuration**:  Understand how to leverage `DEFAULT_CONFIG` and the `init` function to make your module configurable and adaptable to different environments.
* **Testing**:  Get started with testing your router module using the included example tests in `tests/test_core.py` and utility functions in `tests/utils.py`. Writing tests is key to ensuring your module works reliably.
* **Package Structure**:  See the recommended package structure in action. Following this structure will make your module easily integrable with the LitePolis ecosystem.

**What's changed from the base template?**

While building upon the [LitePolis-router Template](https://github.com/NewJerseyStyle/LitePolis-router-template), this example introduces a few key enhancements to get you started faster:

* **Concrete Example Endpoints**:  Instead of just a basic test route, `core.py` now includes example endpoints like `/` and `/user`. These demonstrate how to structure responses using `ResponseMessage` and `UserResponseMessage`, providing a clearer picture of how to build your API logic.
* **Response Models**: The inclusion of `ResponseMessage` and `UserResponseMessage` showcases how to define structured responses using Pydantic models. This is a best practice for building robust and well-documented APIs.

Let's dive into how you can get started and customize this example for your own needs!

## Getting Started

1. **Clone the Repository:**  Your first step is to bring this example to your local machine. Clone the repository using Git:
   ```bash
   git clone <repository_url>
   ```

2. **Rename and Personalize Your Package:**  Make this example your own by renaming it. You'll need to update the package name in a few places:
    * **`setup.py`**: Open `setup.py` and change `name='litepolis-router-example'` to your preferred package name (e.g., `litepolis-router-myfeature`).  Don't forget to also update the `version`, `description`, `author`, and `url` fields to reflect your module.
    * **`tests/test_core.py`**: Navigate to `tests/test_core.py` and adjust the import statement.  If you renamed your package to `litepolis-router-myfeature`, change `from litepolis_router_example import *` to `from litepolis_router_myfeature import *`.
    * **Rename the Root Folder**:  Finally, rename the root folder `litepolis_router_example` to match your new package name (e.g., `litepolis_router_myfeature`).

3. **Craft Your Router Logic in `core.py`:**  This is where the magic happens!
    * **Explore `core.py`**: Open the renamed `core.py` file. This is the heart of your router module.
    * **`APIRouter` Instance (`router`)**:  You'll find an `APIRouter` instance named `router`. This is where you'll define your API endpoints. Think of it as the blueprint for your API. To learn more about FastAPI routers, check out the [FastAPI documentation on Routers](https://fastapi.tiangolo.com/tutorial/bigger-applications/).
    * **Defining Routes**:  See how decorators like `@router.get("/")` and `@router.get("/user")` are used to define GET requests.  You can add more routes using decorators like `@router.post()`, `@router.put()`, `@router.delete()`, etc., for different HTTP methods.  Refer to the [FastAPI path operations documentation](https://fastapi.tiangolo.com/tutorial/path-operations/) for a comprehensive guide.
    * **`prefix` Variable**:  The `prefix` variable is automatically derived from your package name. This prefix will be added to the beginning of all your API routes, ensuring proper organization within LitePolis.
    * **`dependencies` and `DEFAULT_CONFIG`**:  These are initially placeholders.  As you develop your module, you can use `dependencies` to inject dependencies into your endpoints (like authentication or database sessions) and `DEFAULT_CONFIG` to define default configuration settings for your module.
    * **`init(config)` Function**:  The `init(config)` function is vital. LitePolis uses this function to initialize your router module with a configuration object.  Modify this function to set up resources your module needs, such as database connections, external service clients, or load configurations from the provided `config` object.
    * **Example Endpoints**:  Examine the example endpoints (`/` and `/user`). They demonstrate basic routing and how to structure responses using `ResponseMessage` and `UserResponseMessage`.  Replace these example endpoints with your actual API endpoints that implement the functionality you want for your LitePolis module.
    * **Docstrings are Key**:  Make sure to update the docstrings for all your endpoints.  Clear and accurate docstrings are essential for API documentation and for other developers (and your future self!) to understand your code.

4. **Test Your Router with `tests/test_core.py` and `utils.py`:**  Testing is not optional!
    * **`tests/test_core.py`**:  Open `tests/test_core.py`. This file provides example tests using `unittest` and `fastapi.testclient`.  Adapt and expand these tests to thoroughly cover the functionality of your router module.
    * **`utils.py`**:  The `utils.py` file in the `tests` directory contains helpful utility functions like `find_package_name()`. This function makes your tests more robust by dynamically finding your package name, even after renaming. `test_core.py` uses this to import your module correctly.
    * **Testing `init` and `DEFAULT_CONFIG`**:  Pay close attention to how the tests are set up.  They should implicitly or explicitly ensure that `DEFAULT_CONFIG` and the `init` function are used to properly initialize your module for testing. This is especially important if your module relies on configuration settings. Run the tests frequently as you develop to catch issues early!

## Key Files and Modifications

* **`setup.py`**:  This is your package's metadata file.  **The most critical change** is updating the `name` field to your unique package name.  Also, update `version`, `description`, `author`, and `url` as needed to accurately describe your module.

* **`litepolis_router_example/core.py` (renamed)**: This file houses the core logic of your module. It includes the `router` (your `APIRouter` instance), `prefix`, `dependencies`, `DEFAULT_CONFIG`, and the crucial `init` function.  Remember, `init` is essential for LitePolis to initialize and start your module correctly. `DEFAULT_CONFIG` provides default settings. Replace the example endpoints with your own, implementing your desired API operations.  **Crucially, keep your docstrings updated!**  Examine the `ResponseMessage` model and adapt or create new response models as needed to fit your API's data structures.

* **`tests/test_core.py`**:  This file is for testing!  Modify the tests to reflect the changes you make in `core.py`.  Comprehensive testing is vital for ensuring your module is robust and reliable.  Ensure your tests properly utilize `init` and `DEFAULT_CONFIG` for setup. The `find_package_name()` function in `tests/utils.py` helps your tests dynamically adapt to package renaming.

## Important Considerations

* **API Documentation:**  Well-documented APIs are essential for maintainability and collaboration.  Write clear and comprehensive docstrings for all your endpoints in `core.py`.  LitePolis will use these docstrings to generate API documentation automatically. For best practices and examples of API documentation with FastAPI, check out resources like: [How to Document an API for Python FastAPI](https://medium.com/codex/how-to-document-an-api-for-python-fastapi-best-practices-for-maintainable-and-readable-code-a183a3f7f036)

* **Testing is Your Friend:**  Invest time in writing thorough tests that cover all aspects of your router module.  Good tests will save you headaches down the line by helping you catch errors early and ensuring the stability of your code.  The example tests in `tests/test_core.py` and the `find_package_name()` utility in `tests/utils.py` are just starting points – expand upon them!

* **Declare Dependencies in `setup.py`**:  If your module relies on any external Python libraries, list them in the `install_requires` section of `setup.py`. This ensures that these dependencies are automatically installed when your module is deployed.
* **`DEFAULT_CONFIG` and `init` are Key for Initialization**:  The `DEFAULT_CONFIG` dictionary and the `init` function are not just placeholders – they are fundamental for how LitePolis manages and initializes your module.  Make sure you understand how they work and use them correctly in both your `core.py` and your tests.
