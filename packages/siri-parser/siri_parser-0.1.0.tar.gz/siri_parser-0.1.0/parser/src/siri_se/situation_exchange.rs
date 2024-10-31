use serde::{Deserialize, Serialize};


#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct SituationExchange {
    pub situation_exchange_delivery: SituationExchangeDelivery
}