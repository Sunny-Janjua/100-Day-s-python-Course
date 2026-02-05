🖥️ PYTHON os MODULE – ALL OPERATIONS (ONE SLIDE)
📁 Directory Operations

os.getcwd() → current directory

os.chdir(path) → change directory

os.mkdir(name) → create single folder

os.makedirs(path) → create nested folders

os.rmdir(name) → delete empty folder

os.listdir(path) → list files/folders

📄 File Operations

os.remove(file) → delete file

os.rename(old, new) → rename file/folder

os.stat(file) → file info (size, time)

🧭 Path Operations (os.path)

os.path.exists(path) → check exist

os.path.isfile(path) → is file?

os.path.isdir(path) → is folder?

os.path.join(a, b) → join path

os.path.abspath(path) → absolute path

os.path.basename(path) → file name

os.path.dirname(path) → folder path

os.path.split(path) → split path

os.path.getsize(path) → file size

🌍 Environment Variables

os.environ → all variables

os.environ.get("PATH") → get variable

os.environ["KEY"] = "value" → set variable

🖥️ System / OS Info

os.name → OS type

os.getlogin() → current user

os.cpu_count() → CPU cores

os.getpid() → process ID

⚙️ OS Commands

os.system("command") → run command
(dir, ls, etc.)

🛡️ Permissions & Access

os.access(path, os.R_OK) → read access

os.access(path, os.W_OK) → write access

os.chmod(path, mode) → change permission

🔁 Process & Exit

os._exit(0) → force exit program













📁 PYTHON FILE HANDLING – ALL METHODS (ONE SLIDE)
🔑 Open / Close

open(file, mode) → open file

file.close() → close file

📖 Read Methods

file.read() → read complete file

file.readline() → read one line

file.readlines() → read all lines (list)

✍️ Write Methods

file.write(text) → write text

file.writelines(list) → write multiple lines

🔄 File Modes

"r" → read

"w" → write (overwrite)

"a" → append

"x" → create new

"rb" → read binary

"wb" → write binary

🛡️ Best Practice

with open(...) as file: → auto close

🧭 File Pointer

file.tell() → current position

file.seek(pos) → move pointer

🧪 Extra Utilities

file.flush() → clear buffer

file.readable() → can read?

file.writable() → can write?

file.seekable() → can seek?

❌ File Delete (via os)

os.remove(file) → delete file