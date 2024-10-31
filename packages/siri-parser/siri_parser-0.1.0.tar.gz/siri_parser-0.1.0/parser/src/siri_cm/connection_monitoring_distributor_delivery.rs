use serde::{Deserialize, Serialize};



#[derive(Debug, Default, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct ConnectionMonitoringDistributorDelivery {
    version: String, // Version du service, ex: '2.1:FR-IDF-2.4'
    #[serde(flatten)]
    leader: XxxDelivery,
    wait_prolonged_departure: WaitProlonged­Departure, // Contient les informations de prolongation d'attente et autres
    stopping_position_change_departure: StoppingPositionChangeDeparture, // Contient les informations de changement de position et autres
    distribution_departure_cancellation: DistributionDepartureCancellation, // Contient les informations d'annulation de distribution et autres
    extensions: Option<Extensions>, // Emplacement pour extension utilisateur
}
