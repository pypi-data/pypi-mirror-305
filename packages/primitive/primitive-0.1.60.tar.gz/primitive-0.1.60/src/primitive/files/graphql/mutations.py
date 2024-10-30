create_trace_mutation = """
mutation createTrace($input: TraceCreateInput!) {
    traceCreate(input: $input) {
        ... on Trace {
            id
            signalId
            signalName
        }
    }
}
"""
