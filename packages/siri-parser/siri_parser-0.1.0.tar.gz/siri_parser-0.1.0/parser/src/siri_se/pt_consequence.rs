


#[derive(Debug)]
pub struct PtConsequence {
    /// Classification of the effect on the service.
    /// Can be replaced by JourneyCondition in AffectedVehicleJourney.
    classifiers: Vec<Condition>, // 0:*

    /// Severity of the situation. Default is normal.
    severity: Severity, // 1:1

    /// Advice to passengers.
    advice: Option<PtAdviceStructure>, // 0:1

    /// How the disruption should be managed in information systems.
    blocking: Option<Blocking>, // 0:1

    /// Public targeted by the situation.
    activity: Option<BoardingActivity>, // 0:1

    /// Anticipated delays.
    delay: Option<Delays>, // 0:1
}