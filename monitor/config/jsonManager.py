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
import json

def addTarget(name:str, ip:str):
    try:
        print("configManager: Creating config.json")
        config = open("monitor.json", "a+")
        print("configManager: Writing to config.json")
        config.close()
        with open("monitor.json", "r") as jsonFile:
            monitordata = json.load(jsonFile)
            jsonFile.close()
            monitordata["targets"][name] = {}
            monitordata["targets"][name]["ip"] = ip
            monitordata["targets"]["target-list"].append(name)
            jsonFile = open("monitor.json", "w+")
            jsonFile.write(json.dumps(monitordata, indent=4, sort_keys=True))
            jsonFile.close()
            return True;
    except IOError:
        print("ERROR: Experienced IO Error when creating config.json")
        return False;


def addEmail(email:str, ip:str):
    try:
        with open("monitor.json", "r") as jsonFile:
            monitordata = json.load(jsonFile)
            jsonFile.close()
            monitordata["emails"].append(email)
            jsonFile = open("monitor.json", "w+")
            jsonFile.write(json.dumps(monitordata, indent=4, sort_keys=True))
            jsonFile.close()
            return True;
    except IOError:
        print("ERROR: Experienced IO Error when creating config.json")
        return False;



def delTarget(name:str):
    try:
        with open("monitor.json", "r") as jsonFile:
            monitordata = json.load(jsonFile)
            jsonFile.close()
            del monitordata["targets"][name]
            monitordata["targets"]["target-list"].remove(name)
            jsonFile = open("monitor.json", "w+")
            jsonFile.write(json.dumps(monitordata, indent=4, sort_keys=True))
            jsonFile.close()
            return True;
    except IOError:
        print("ERROR: Experienced IO Error when creating config.json")
        return False;