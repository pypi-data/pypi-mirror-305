


#[derive(Debug)]
pub struct PublishingActions {
    pub publish_to_web: Vec<PublishToWebAction>,
    pub publish_to_mobile: Vec<PublishToMobileAction>,
    pub publish_to_display: Vec<PublishToDisplayAction>,
    pub notify_by_email: Vec<NotifyByEmailAction>,
    pub notify_by_sms: Vec<NotifyBySmsAction>,
}