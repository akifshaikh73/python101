def main():

    #profiles=['271562797580_AccentureFullAdmin','271562797580_AccentureFullAdmin', '567729715457_AccentureFullAdmin', '759141350787_AccentureFullAdmin', '335629769328_AccentureFullAdmin', '839113706656_AccentureFullAdmin', '987078416329_AccentureFullAdmin', '471105749344_AdministratorAccess', '669693036398_AccentureFullAdmin', '997604121474_AccentureFullAdmin', '707168858567_AccentureFullAdmin', '962475949940_AccentureFullAdmin', '959968060638_AccentureFullAdmin', '591381282041_AWSAdministratorAccess', '381067379246_AWSAdministratorAccess', '736577165083_AWSAdministratorAccess', '870767228284_AWSAdministratorAccess', '630403223534_AWSAdministratorAccess', '778297066104_AWSAdministratorAccess', '205474830480_AWSAdministratorAccess', '248969292625_AccentureFullAdmin', '007627281016_AWSAdministratorAccess', '812777871027_AWSAdministratorAccess', '883685621503_AccentureFullAdmin', '774917615573_AccentureFullAdmin', '443252421478_AccentureFullAdmin', '347573372292_AccentureFullAdmin', '303420442075_AccentureFullAdmin', '347575916305_AccentureFullAdmin' '567729715457_AccentureFullAdmin', '759141350787_AccentureFullAdmin', '335629769328_AccentureFullAdmin', '839113706656_AccentureFullAdmin', '987078416329_AccentureFullAdmin', '471105749344_AdministratorAccess', '669693036398_AccentureFullAdmin', '997604121474_AccentureFullAdmin', '707168858567_AccentureFullAdmin', '962475949940_AccentureFullAdmin', '959968060638_AccentureFullAdmin', '591381282041_AWSAdministratorAccess', '381067379246_AWSAdministratorAccess', '736577165083_AWSAdministratorAccess', '870767228284_AWSAdministratorAccess', '630403223534_AWSAdministratorAccess', '778297066104_AWSAdministratorAccess', '205474830480_AWSAdministratorAccess', '248969292625_AccentureFullAdmin', '007627281016_AWSAdministratorAccess', '812777871027_AWSAdministratorAccess', '883685621503_AccentureFullAdmin', '774917615573_AccentureFullAdmin', '443252421478_AccentureFullAdmin', '347573372292_AccentureFullAdmin', '303420442075_AccentureFullAdmin', '347575916305_AccentureFullAdmin']
    profiles=['347575916305_AccentureFullAdmin']
    regions = ['us-east-1', 'us-west-2']
    csv_name = 'sg_details-'
    timestamp = time.strftime("%Y-%m-%d-%H-%M")

    final_sgs=[]
    for profile in profiles:
        session = boto3.session.Session(profile_name=profile)

        #Call get_sg function to get security group details
        sgs=get_sg(session,regions,profile)
        final_sgs = final_sgs + sgs
        # create_csv(final_sgs,csv_name,timestamp)
        filename = profile.split('_')[0] + '.json'
        with open(filename, 'w') as fp:
            json.dump(final_sgs, fp)


