use serde::{Deserialize, Serialize};


#[derive(Debug, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "PascalCase")]
pub struct SituationExchangeDelivery {
    pt_situation_context: Option< Vec<PtSituationContext>>,
    situations: Option<Vec<Situation>>,
    pt_situation_element: Option<Vec<PtSituationElement>>
}