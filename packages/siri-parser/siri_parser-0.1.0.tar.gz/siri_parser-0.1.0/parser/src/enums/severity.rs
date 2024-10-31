use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "camelCase")]
enum Severity {
    Unknown,   // Inconnu
    Slight,    // Léger
    Normal,    // Normal
    Severe,    // Sévère
    NoImpact,  // Pas d’impact
    Undefined, //Non défini
}
