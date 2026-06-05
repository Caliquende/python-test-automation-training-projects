# Newman API Collection

This folder stores exported Postman files used for Newman practice.

Files:

* `collection/collection.json`
* `environment/environment.json`

The collection uses public fake API base URLs:

* `https://jsonplaceholder.typicode.com`
* `https://dummyjson.com`

No GitHub Secrets are required for Newman because these requests use public demo APIs.

## Scenarios

Positive scenarios:

* JSONPlaceholder GET All Posts
* JSONPlaceholder GET Single Post
* JSONPlaceholder POST Create Post
* DummyJSON GET All Products
* DummyJSON GET Single Product
* DummyJSON POST Add Product

Negative scenarios:

* JSONPlaceholder GET Non Existing Post
* JSONPlaceholder GET Wrong Endpoint
* DummyJSON GET Non Existing Product
* DummyJSON GET Wrong Product Endpoint

Data not found means the resource path is valid but the requested item does not exist. Wrong endpoint means the route itself is invalid.

## Local Windows PowerShell Commands

CLI only:

```powershell
newman run ".\api\newman\collection\collection.json" -e ".\api\newman\environment\environment.json"
```

CLI + HTML:

```powershell
newman run ".\api\newman\collection\collection.json" -e ".\api\newman\environment\environment.json" -r "cli,html" --reporter-html-export ".\reports\newman-report.html"
```

CLI + JUnit XML:

```powershell
newman run ".\api\newman\collection\collection.json" -e ".\api\newman\environment\environment.json" -r "cli,junit" --reporter-junit-export ".\reports\newman-report.xml"
```

CLI + HTML + JUnit XML:

```powershell
newman run ".\api\newman\collection\collection.json" -e ".\api\newman\environment\environment.json" -r "cli,html,junit" --reporter-html-export ".\reports\newman-report.html" --reporter-junit-export ".\reports\newman-report.xml"
```

Report paths:

* `reports/newman-report.html`
* `reports/newman-report.xml`

Generated reports must not be committed.

Current expected result:

* 10 requests
* 10 test scripts
* 40 assertions
* 0 failed
