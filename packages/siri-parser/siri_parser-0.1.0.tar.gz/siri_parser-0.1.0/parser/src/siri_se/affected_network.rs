


#[derive(Debug)]
pub struct AffectedNetwork {
    pub operators: Vec<AffectedOperator>,   // Annotation to the impacted service operators
    pub network: Option<NetworkRef>,         // Reference to the network of the affected line
    pub network_name: Vec<String>,           // Names of the affected network(s)
    pub routes_affected: Vec<String>,        // Textual description of affected routes
    pub mode: Option<AffectedModeGroup>,     // Identification of impacted modes
    pub lines: Option<NetworkLines>,         // Scope of the affected lines
}