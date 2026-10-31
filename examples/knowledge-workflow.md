# Example: a synthetic onboarding question

This example explains the product flow. It is not a runnable deployment or customer data.

**Synthetic source:** “Every new project begins with an approved scope, a named owner, and an agreed usage budget. Review source citations before sharing an answer externally.”

**Question:** “What is required before starting a project?”

1. An administrator adds the synthetic text to a tenant's knowledge library.
2. An authorized member submits the question in that workspace.
3. The gateway checks the tenant's model permission and applicable usage controls.
4. Retrieval finds the relevant passage within that tenant.
5. Local mode returns the passage with a source citation. A configured cloud model could instead generate an answer from the question and passages.
6. The application records usage. If submitted as a workflow, the user can inspect its state and output after a worker processes it.

**A useful result:** the passage supports an answer identifying approved scope, a named owner, and an agreed budget. An authorized person can inspect the evidence before relying on it.

**A different tenant:** should receive none of the first tenant's passages. Tenant separation is tested in the private foundation.

**A provider timeout:** may leave a reserved amount requiring reconciliation. Retrying with a fresh key could duplicate billable work, so the product preserves the request identity and surfaces the uncertain outcome.
