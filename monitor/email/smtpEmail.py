"""

The A86Monitor program, its documentation, and any other auxiliary resources involved in building, installing
and running the program are licensed under the GNU General Public License. This includes,
but is not limited to, all the files in the official source distribution, as well as the source distribution itself.

A copy of the GNU General Public License can be found in the file LICENSE in the top directory of the official
source distribution.
The license is also available in several formats through the World Wide Web,
via http://www.gnu.org/licenses/licenses.html#GPL,
 or you can write the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

A86Monitor is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

def sendFailureEmail(email:str, target:str, sender:str, password:str, sender_name:str, sender_server:str, sender_port:int):

    msg = EmailMessage()
    msg['Subject'] = target + " has gone down"
    msg['From'] = sender
    msg['To'] = email
    message = target + """ has appeared to have gone offline. If you have failover setup on this target, it has now 
    switched over to it. You will receive a notification when it comes back online.

    ~ A86Monitor
    """
    msg.set_content(message)


    try:
        smtpObj = smtplib.SMTP(sender_server,port=sender_port)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(sender, password)
        smtpObj.send_message(msg,sender, email)
        print
        "Successfully sent email"
        print("test")
    except smtplib.SMTPException as ex:
        print(
        "Error: unable to send email")

def sendRestoredEmail(email:str, target:str, sender:str, password:str, sender_name:str, sender_server:str, sender_port:int):
    msg = EmailMessage()
    msg['Subject'] = target + " Connection Restored"
    msg['From'] = sender
    msg['To'] = email
    message = target + """ has been restored.

    ~ A86Monitor
    """
    msg.set_content(message)
    try:
        smtpObj = smtplib.SMTP(sender_server,port=sender_port)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(sender, password)
        smtpObj.send_message(msg, sender, email)
        print
        "Successfully sent email"
    except smtplib.SMTPException as ex:
        print(
        "Error: unable to send email")