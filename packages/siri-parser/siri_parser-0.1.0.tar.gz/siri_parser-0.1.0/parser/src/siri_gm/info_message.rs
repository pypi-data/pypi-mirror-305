use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct InfoMessage {
    format_ref: String,                // FormatCode - always "France" for this profile
    recorded_at_time: DateTime<Utc>,   // Heure d'enregistrement du message
    identity: ItemIdentifier,          // Identifiant unique du message SIRI
    info_message_identifier: String,   // Identifiant InfoMessage
    info_message_version: Option<u32>, // Version du InfoMessage
    info_channel_ref: String,          // Canal auquel appartient le message
    valid_until_time: DateTime<Utc>,   // Date et heure jusqu'à laquelle le message est valide
    situation_refs: Vec<SituationCode>, // Référence à des événements externes
    content: String,                   // Le message lui-même
    extensions: Option<Extensions>,    // Emplacement pour extension utilisateur
}
