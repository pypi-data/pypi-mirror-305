use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
struct InfoMessageCancellation {
    recorded_at_time: DateTime<Utc>, // Heure à laquelle le message a été annulé
    identity: ItemIdentifier,        // Identifiant unique du message SIRI
    info_message_identifier: String, // Référence InfoMessage du message à annuler
    info_channel_ref: Option<String>, // Canal auquel appartient le message
    extensions: Option<Extensions>,  // Emplacement pour extension utilisateur
}
