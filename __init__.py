from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

__author__ = 'klarsen14'
LOGGER = LOG.create_logger( __name__ )

class PunSkill( MycroftSkill ):

    def __init__( self ):
        super( PunSkill, self ).__init__( name="PunSkill" )
        LOGGER.info( "__init__" )

    @intent_handler( IntentBuilder( "" ).require( "pun" ) )
    def handle_pun_intent( self, message ):
        LOGGER.info( "pun" )
        self.speak_dialog( "pun", data={} )

def create_skill():
    return PunSkill()
