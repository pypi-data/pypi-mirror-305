use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "camelCase")]
enum SourceType {
    DirectReport, // Rapport remis en direct
    Email,        // Rapport reçu via email
    Phone,        // Rapport reçu via téléphone
    Post,         // Rapport reçu via courrier postal
    Feed,         // Rapport reçu via alimentation automatique
    Radio,        // Rapport reçu via radio
    TV,           // Rapport reçu via TV
    Web,          // Rapport reçu via website
    Text,         // Rapport reçu via message
    Other,        // Rapport reçu via autres moyens
}
