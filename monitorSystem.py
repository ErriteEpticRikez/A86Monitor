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
import ping3
from errors import PingError

from monitor.email.smtpEmail import sendFailureEmail, sendRestoredEmail
import json
import time
from ping3 import verbose_ping

ping3.EXCEPTIONS = True
stop = False
targets = None
failed_targets = []
print("A86Monitor V1.1")
with open("monitor.json", "r") as jsonFile:
    monitordata = json.load(jsonFile)
    jsonFile.close()
    targets = monitordata["targets"]

while not stop:
    for target in targets["target-list"]:
        target_prev_failed = True
        try:
            verbose_ping(monitordata["targets"][target]["ip"], count=10)
            try:
                index = failed_targets.index(target)
            except KeyError:
                target_prev_failed = False
            except ValueError:
                target_prev_failed = False
            if target_prev_failed:
                failed_targets.remove(target)
                sendRestoredEmail(email, target, monitordata["sender"], monitordata["password"],
                                  monitordata["sender-name"], monitordata["sender-server"], monitordata["sender-port"])
        except PingError as Ex:
            try:
                smindex = failed_targets.index(target)
                print("We already sent an email regarding this target. Ignoring")
            except ValueError:
                for email in monitordata["emails"]:
                    sendFailureEmail(email, target, monitordata["sender"], monitordata["password"],
                                     monitordata["sender-name"], monitordata["sender-server"], monitordata["sender-port"])
                    failed_targets.append(target)
    time.sleep(30)
