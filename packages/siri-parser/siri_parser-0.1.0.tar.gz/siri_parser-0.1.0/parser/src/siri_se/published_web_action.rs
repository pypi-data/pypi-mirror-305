



#[derive(Debug)]
pub struct PublishToWebAction {
    pub parameterized_action: Option<ParameterizedAction>,
    pub incidents: Option<bool>,       // Defaults to true
    pub home_page: Option<bool>,       // Defaults to false
    pub ticker: Option<bool>,          // Defaults to false
    pub social_network: Vec<String>,   // e.g., "twitter.com", "facebook.com"
}