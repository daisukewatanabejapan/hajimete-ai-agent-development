# AGENTS.md

## About this project

This is a Java project for [describe its purpose].

## Repository map

- `src/main/java/`: application code
- `src/test/java/`: tests
- `pom.xml` or `build.gradle`: build configuration

Change this map to match your repository.

## Working rules

- Change only what the task requires.
- Do not change public API behavior unless requested.
- Add a regression test when fixing a bug where practical.
- Explain why a new dependency is needed.
- Do not edit generated files by hand.
- Never add API keys or passwords to the code.

## Checks

Keep only the commands your project uses.

For Maven:

    ./mvnw test
    ./mvnw verify

For Gradle:

    ./gradlew test
    ./gradlew check

## Completion report

- What changed
- Commands run and their results
- Checks that could not be run and why
