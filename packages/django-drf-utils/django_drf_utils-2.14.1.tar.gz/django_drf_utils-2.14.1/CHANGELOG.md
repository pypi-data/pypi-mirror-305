# Changelog

All notable changes to this project will be documented in this file.

## [2.14.1](https://gitlab.com/biomedit/django-drf-utils/-/releases/2%2E14%2E1) - 2024-10-31

[See all changes since the last release](https://gitlab.com/biomedit/django-drf-utils/compare/2%2E14%2E0...2%2E14%2E1)


### 🐞 Bug Fixes

- **NamedField:** Accept `+` characters ([aaa1db0](https://gitlab.com/biomedit/django-drf-utils/commit/aaa1db00871f421a1478d1c55ad5dc7884ffcb24)), Close #18

### 🧱 Build system and dependencies

- Add bumpversion script ([697d196](https://gitlab.com/biomedit/django-drf-utils/commit/697d1961d81df10ea848c82f067bad575ee341f7))
- Migrate setup.cfg to pyproject.toml ([8a7fed9](https://gitlab.com/biomedit/django-drf-utils/commit/8a7fed9de046e76c51e8db7bfd499f86db58f6d4))

### 👷 CI

- Use modern tools ([cb548ce](https://gitlab.com/biomedit/django-drf-utils/commit/cb548ce1fbf5801b8974a62e3b442e927f9ce7b2))

### 📝 Documentation

- Clean up README ([66d56d6](https://gitlab.com/biomedit/django-drf-utils/commit/66d56d69d3dd23bd9808d57a6b0cb009de626f8b))

### 🧹 Refactoring

- Fix ruff warnings ([53d3927](https://gitlab.com/biomedit/django-drf-utils/commit/53d3927f65296e88c5f033b675574aaf67d4efb8))

### 🎨 Style

- Format changelog ([518f97e](https://gitlab.com/biomedit/django-drf-utils/commit/518f97e2a7f7198a1b831171dc7d0e206e81dfb4))

### ✅ Test

- Run tests on Python 3.13 ([aef8816](https://gitlab.com/biomedit/django-drf-utils/commit/aef881656223c7102d8b8b0b06b0de2b0dad349f))

## [2.14.0](https://gitlab.com/biomedit/django-drf-utils/-/releases/2%2E14%2E0) - 2023-07-19

[See all changes since the last release](https://gitlab.com/biomedit/django-drf-utils/compare/2%2E13%2E1...2%2E14%2E0)

### Features

- **config:** Add `OidcMapper` to `Oidc` ([55b17c9](https://gitlab.com/biomedit/django-drf-utils/commit/55b17c969d8668411744a283ec873ee3a2f5cf07))

## [2.13.0](https://gitlab.com/biomedit/django-drf-utils/-/releases/2%2E13%2E0) - 2023-06-27

[See all changes since the last release](https://gitlab.com/biomedit/django-drf-utils/compare/2%2E12%2E0...2%2E13%2E0)

### Features

- **models:** Add EmailField ([e74945e](https://gitlab.com/biomedit/django-drf-utils/commit/e74945e8ad536cf919919f3809335999739e65cf))

## [2.12.0](https://gitlab.com/biomedit/django-drf-utils/-/releases/2%2E12%2E0) - 2023-06-21

[See all changes since the last release](https://gitlab.com/biomedit/django-drf-utils/compare/2%2E11%2E0...2%2E12%2E0)

### Features

- **email:** Allow empty recipients ([4a8c7ce](https://gitlab.com/biomedit/django-drf-utils/commit/4a8c7ceb3b26872419904e7cdb97950c49f46874))

## [2.11.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.10.0...2.11.0) (2023-04-26)

### Features

- **permissions:** add IsPost and IsPatch permission classes ([0bc9459](https://gitlab.com/biomedit/django-drf-utils/commit/0bc94594e069acac94f47e96bedd1b09e74ddfd4))

## [2.10.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.9.0...2.10.0) (2023-01-30)

### Features

- **permissions:** add generic request http method permission classes ([0fa0d3d](https://gitlab.com/biomedit/django-drf-utils/commit/0fa0d3db1e439d7a6d529cdc82d481066dada030)), closes [#12](https://gitlab.com/biomedit/django-drf-utils/issues/12)

## [2.9.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.8.0...2.9.0) (2023-01-12)

### Features

- **models/NodeField:** add underscore to allowed characters ([1ec45e4](https://gitlab.com/biomedit/django-drf-utils/commit/1ec45e452d59a3e7fb70f6492a4a7a66d7c0ad89)), closes [#11](https://gitlab.com/biomedit/django-drf-utils/issues/11)

## [2.8.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.7.2...2.8.0) (2022-12-22)

### Features

- **factories:** extend DjangoModelFactory and mute Django signals ([a73a24f](https://gitlab.com/biomedit/django-drf-utils/commit/a73a24ff80fd3c0187bbeabcbfc602cf178561eb)), closes [#10](https://gitlab.com/biomedit/django-drf-utils/issues/10)

### [2.7.2](https://gitlab.com/biomedit/django-drf-utils/compare/2.7.1...2.7.2) (2022-12-14)

### [2.7.1](https://gitlab.com/biomedit/django-drf-utils/compare/2.7.0...2.7.1) (2022-12-14)

## [2.7.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.6.0...2.7.0) (2022-09-21)

### Features

- **exception_logger:** log client-side exceptions at the WARNING level ([3e97c8a](https://gitlab.com/biomedit/django-drf-utils/commit/3e97c8ab0999a395073a927a281d7e2d3f7f5be2)), closes [#8](https://gitlab.com/biomedit/django-drf-utils/issues/8)

## [2.6.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.5.0...2.6.0) (2022-08-11)

### Features

- add `DetailedValidationInfo` ([74c5706](https://gitlab.com/biomedit/django-drf-utils/commit/74c57066372feb97fc1fbdf2828ac17fb13afdb9))

## [2.5.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.4.0...2.5.0) (2022-08-08)

### Features

- **config:** add support for UnionType ([08c95e0](https://gitlab.com/biomedit/django-drf-utils/commit/08c95e0e9208dba7be2b3dca1d98b5e82b15d42b)), closes [#7](https://gitlab.com/biomedit/django-drf-utils/issues/7)

## [2.4.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.3.0...2.4.0) (2022-05-23)

### Features

- do not log exceptions of class UnprocessableEntityError as ERROR ([ea7b1b8](https://gitlab.com/biomedit/django-drf-utils/commit/ea7b1b8ea4c36396ca2add3a7ed2012dacda687d)), closes [#5](https://gitlab.com/biomedit/django-drf-utils/issues/5)

## [2.3.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.2.1...2.3.0) (2022-03-28)

### Features

- **exceptions:** add `UnprocessableEntityError` ([a33109c](https://gitlab.com/biomedit/django-drf-utils/commit/a33109c23f1259290b088cadeefd667a2d4b7312))

### [2.2.1](https://gitlab.com/biomedit/django-drf-utils/compare/2.2.0...2.2.1) (2021-12-22)

### Bug Fixes

- **UniqueSchema:** improve schema generation for unique_check ([0e8b077](https://gitlab.com/biomedit/django-drf-utils/commit/0e8b0770d69e85401e4a7ed8115fc3a07acb5fd1)), closes [#3](https://gitlab.com/biomedit/django-drf-utils/issues/3)

## [2.2.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.1.0...2.2.0) (2021-12-01)

### Features

- **tests/utils:** add fixture `patch_request_side_effect` to define a side effect when mocking requests ([2f71d1d](https://gitlab.com/biomedit/django-drf-utils/commit/2f71d1d4b00dab99b48435da7f0a5f0a328bed02))

### Bug Fixes

- add [@dataclass](https://gitlab.com/dataclass) to config.BaseConfig ([704d6da](https://gitlab.com/biomedit/django-drf-utils/commit/704d6dacd9aa1a0ac628a67fbcec0bd83b75ce38))

## [2.1.0](https://gitlab.com/biomedit/django-drf-utils/compare/2.0.0...2.1.0) (2021-08-20)

### Features

- Add path field to config.Logging ([3c88fbc](https://gitlab.com/biomedit/django-drf-utils/commit/3c88fbc6391cc0ba2f4c39f9196507b419caef96))

## [2.0.0](https://gitlab.com/biomedit/django-drf-utils/compare/1.2.2...2.0.0) (2021-08-11)

### ⚠ BREAKING CHANGES

- **email.sendmail:** email.sendmail no longer uses settings.CONFIG.email

The `sendmail` function no longer depends on `settings.CONFIG`,
which might not be defined in the project. The function now accepts
the explicit `email_cfg` argument.

### Features

- add config module ([ebf0fcc](https://gitlab.com/biomedit/django-drf-utils/commit/ebf0fcc360c94c531c35f6edff12dc1cc2f46a3d))

### Bug Fixes

- **config.BaseConfig:** do not modify the input dictionary ([77dc76c](https://gitlab.com/biomedit/django-drf-utils/commit/77dc76cf9f51c1efc28e78c34e4ad6e9f1e93ded))
- **email.sendmail:** remove implicit dependency on settings.CONFIG.email ([5e994f3](https://gitlab.com/biomedit/django-drf-utils/commit/5e994f36d4e5d829389cfe36c2f727259fb15ad6))

### [1.2.2](https://gitlab.com/biomedit/django-drf-utils/compare/1.2.1...1.2.2) (2021-07-13)

### Bug Fixes

- **unique_check:** ensure no error is thrown when a field is not unique ([cece186](https://gitlab.com/biomedit/django-drf-utils/commit/cece186995f92f8d22131534e4de29f919798537)), closes [portal#395](https://gitlab.com/biwg/libweb/portal/issues/395)

### [1.2.1](https://gitlab.com/biomedit/django-drf-utils/compare/1.2.0...1.2.1) (2021-07-09)

## [1.2.0](https://gitlab.com/biomedit/django-drf-utils/compare/1.1.0...1.2.0) (2021-07-09)

### Features

- **models:** add some utility methods and classes related to models ([a0ff7ee](https://gitlab.com/biomedit/django-drf-utils/commit/a0ff7eeee9a2e2c03089002a67076aa151612cba))

## [1.1.0](https://gitlab.com/biomedit/django-drf-utils/compare/1.0.3...1.1.0) (2021-06-28)

### Features

- **serializers/utils:** add utility method `update_related_fields` ([648c3c3](https://gitlab.com/biomedit/django-drf-utils/commit/648c3c3cb8b65dc575b5fcc59dc51df21007ba44))

### [1.0.3](https://gitlab.com/biomedit/django-drf-utils/compare/1.0.2...1.0.3) (2021-06-23)

### [1.0.2](https://gitlab.com/biomedit/django-drf-utils/compare/1.0.1...1.0.2) (2021-06-04)

### Bug Fixes

- move test utils to the main package ([c0c5fee](https://gitlab.com/biomedit/django-drf-utils/commit/c0c5fee713369bd078ed4f556c71f786e33f42cc))

### [1.0.1](https://gitlab.com/biomedit/django-drf-utils/compare/1.0.0...1.0.1) (2021-06-03)

## 1.0.0 (2021-06-01)
