# Reproducibility

## Supported Environment

Environment Modules compose the workspace engineering environment. Record each validated combination and its scope here. A combination may serve the workspace, several child repositories, or one child repository; environment composition remains workspace-owned.

When a real combination is needed, keep its directly sourceable entry point under `env/<name>.csh` and its modulefiles under `env/modulefiles/`. A typical entry script purges modules, adds the workspace modulefile path, loads the validated tools, and lists the result. Do not create placeholder combinations, a profile framework, or require one universal environment.

## Dependencies

Use modulefiles to select and compose already available source trees, toolchains, Conda environments, and external engineering tools. Modulefiles configure paths and variables; they do not clone, build, test, install, or download.

Prefer version-controlled Conda environment YAML when dependencies fit Conda. Use pip only inside an appropriate Conda environment when necessary. Keep host/system tools outside Conda when Environment Modules are the appropriate selector. Missing host tools are explicit prerequisites; automation must not install them without authorization.

## Setup

```bash
./scripts/project setup
```

State `NOT_IMPLEMENTED` or `UNAVAILABLE` when setup is not yet a supported capability.

## Build

```bash
./scripts/project build
```

State `NOT_IMPLEMENTED` or `UNAVAILABLE` when build is not yet supported.

## Test

```bash
./scripts/project test
```

State `NOT_IMPLEMENTED` or `UNAVAILABLE` when test is not yet supported.

## Verify

```bash
./scripts/project verify
```

Document exactly which currently claimed baseline and capabilities this validates. Do not imply unsupported capabilities were checked.

## Status

```bash
./scripts/project status
```

This command is observational and reports supported, unavailable, and not-yet-implemented capabilities honestly.

## Configuration

Document required configuration, environment variables, defaults, generated configuration, and secret-handling expectations.

## Artifacts

Document generated outputs, source-controlled artifacts, external assets, and temporary outputs.

For formal engineering documents, preserve AsciiDoc (`.adoc`) as the reviewable source and generate PDF only with Asciidoctor PDF. Add thin deterministic generation automation when an actual document requires it; HTML, EPUB, Antora, and documentation-site infrastructure are outside the default architecture.

For data-driven figures, preserve source data and a reproducible project-native or script-based generator where appropriate. For conceptual diagrams, preserve `.drawio` source and generate SVG with draw.io CLI. The currently validated known-good configuration is draw.io Desktop 31.3.2 using `--export --format svg --svg-theme light`; its macOS validation path is `/Applications/draw.io.app/Contents/MacOS/draw.io`. This is evidence for one tested environment, not a universal location or compatibility guarantee. Check the tool only when the current Task changes or regenerates a conceptual diagram, and do not install or change it automatically.

## Reproducing Important Results

## Known Reproducibility Gaps
