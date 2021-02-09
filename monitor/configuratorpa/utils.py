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
def combineTargetsStringList(targets):
    currentid = 1
    results = "Please select a target from the list: \n"
    for target in targets:
        results = results + str(currentid) + ". " + target + "\n"
        currentid = currentid + 1
    return results
