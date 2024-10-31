

#[derive(Debug)]
pub struct PublishToDisplayAction {
    pub parameterized_action: Option<ParameterizedAction>,
    pub on_place: Option<bool>,        // Defaults to true
    pub onboard: Option<bool>,         // Defaults to false
}