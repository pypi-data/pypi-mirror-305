use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct GeneralMessageDelivery {
    pub info_message: Option<InfoMessage>,
    pub info_message_cancellation: Option<InfoMessageCancellation>,
}
