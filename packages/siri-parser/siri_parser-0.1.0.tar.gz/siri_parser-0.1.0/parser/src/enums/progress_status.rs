use serde::{Deserialize, Serialize};

/// 	Une situation ‘open’ n’est pas communiquée à l’extérieur du système. Dès lors que la situation est échangée avec l’extérieur le status doit passer à ‘published’.
#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "camelCase")]
enum ProgressStatus {
    Open,      // Situation en cours
    Published, // Situation en cours et publiée
    Closed,    // Situation terminée
}
