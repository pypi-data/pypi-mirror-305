


#[derive(Debug)]
pub struct PublishToMobileAction {
    pub parameterized_action: Option<ParameterizedAction>,
    pub incidents: Option<bool>,       // Defaults to true
    pub home_page: Option<bool>,       // Defaults to false
}