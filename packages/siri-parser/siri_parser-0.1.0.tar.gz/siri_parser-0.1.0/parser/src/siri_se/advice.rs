


#[derive(Debug)]
pub struct Advice {
    /// Identifier for the advice standard.
    advice_ref: Option<String>, // 0:1

    /// Additional textual advice for passengers.
    details: Vec<String>, // 0:*
}