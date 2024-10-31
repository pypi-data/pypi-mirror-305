use serde::{Deserialize, Serialize};


#[derive(Debug, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "PascalCase")]
pub struct Boarding {
    arrival_boarding_activity: Option<ArrivalBoardingActivity>,
    departure_boarding_activity: Option<DepartureBoardingActivity>
}