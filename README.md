# Windows Server Configurations

## Remote Drive/Folder/Files Share in LAN network with administrative rights (i.e with $)
Ip = 2.2.2.243 (Any Server IP)

If you can access `\\2.2.2.243\c` without the "$" (administrative share), but not `\\2.2.2.243\c$`, it indicates that the administrative share is not enabled or accessible on the target computer.

By default, administrative shares are hidden and accessible only to users with administrative privileges. It's possible that the administrative share `\\2.2.2.243\c$` is disabled or restricted on the target computer, which is why you are unable to access it.

### To enable administrative shares on the target computer, you can try the following steps:
1. Open the Registry Editor by pressing Windows Key + R, then typing "regedit" and pressing Enter.
2. Navigate to the following key:
   `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`
3. Look for a value named `LocalAccountTokenFilterPolicy`. If it exists, double-click on it and set its value to `1`. If the value doesn't exist, you can create it as a DWORD value and set it to `1`.
4. Close the Registry Editor.
5. Restart the target computer to apply the changes.

After restarting the computer, try accessing the administrative share `\\2.2.2.243\c$` again. If the administrative share is now enabled and accessible, you should be able to access it without the "Access Denied" error.

Please note that modifying the registry can have unintended consequences, so it's important to be cautious and create a backup before making any changes. Additionally, enabling administrative shares can pose security risks, so it's recommended to use them judiciously and restrict access to trusted users or administrators.
