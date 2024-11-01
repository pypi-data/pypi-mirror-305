import psutil
import sympy


def calculator(expr: str) -> float | str:
    """
        When to use this function: Don't calculate any math problems by yourself, you are not good at math,
        you must use this function to calculate **all** the math calculations, this is the rule you must follow seriously.

        What does this function do: Calculates the result of a mathematical expression containing only constant numbers.

        This function takes a string representing a mathematical expression as input,
        simplifies it using SymPy's simplify function, and returns the result as a float.

        Args:
            expr (str): A mathematical expression consisting of constant numbers !!!

        Returns:
            float | str: The numerical result of the evaluated expression as a float,
                    or an error message as a string if the expression is invalid or cannot be evaluated.

        Raises:
            sympy.SympifyError: If the input expression is not a valid mathematical expression.
    """
    expr = expr.replace(',', '')
    expr = expr.replace('_', '')
    try:
        return sympy.simplify(expr, rational=None)
    except sympy.SympifyError as se:
        return se.__repr__()


def show_specifications_of_current_computer(**kwargs) -> str:
    """
        Returns a string representation of the current computer's hardware specifications.

        You may need unit conversions before you generate the answers, don't forget to calculate them with "constant_calculate"
        For example: the unit Mhz should be converted to GHz, the unit Bytes may be converted to Gigabytes(GB)...

        This function collects various hardware information, including CPU details, memory, swap_memory, disk partitions, disk usage,
        network I/O, and network interfaces.

        Args:
            **kwargs: Arbitrary keyword arguments (not used in this function).

        Returns:
            str: A JSON-style string containing the computer's hardware specifications.
    """
    return str({
        'cpu_logical_cores': psutil.cpu_count(logical=True),
        'cpu_physical_cores': psutil.cpu_count(logical=False),
        'cpu_frequency(Mhz)': psutil.cpu_freq(),
        'memory(Byte)': psutil.virtual_memory(),
        'swap_memory(Byte)': psutil.swap_memory(),
        'disk_partitions': psutil.disk_partitions(),
        'disk_usage(Byte)': psutil.disk_usage('/'),
        'net_io(Byte)': psutil.net_io_counters(),
        'net_interfaces': psutil.net_if_addrs()
    })


def find_all_processes(**kwargs) -> str:
    """
        Retrieves and displays information about all running processes on the system,
        if you are not clear about which process you are looking for, you should retrieve all processes first.

        This function iterates over all processes, collecting details
        such as process ID, name, user, status, creation time, CPU usage, and
        memory usage. The collected data is stored in a dictionary and returned as a
        string representation.

        Args:
            **kwargs: Accepts any keyword arguments (currently not used).

        Returns:
            str: A string representation of a dictionary containing process information.
    """
    all_processes = dict()
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            all_processes[proc.name()] = {
                'pid': proc.pid,
                'name': proc.name(),
                'user': proc.username(),
                'status': proc.status(),
                'create_time': proc.create_time(),
                'cpu_percent': proc.cpu_percent(interval=0.1),
                'memory_percent': proc.memory_percent()
            }
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            pass
    return str(all_processes)


def find_top_k_processes_with_the_highest_cpu_usage(top_k: int = 6) -> str:
    """
        Finds the top K processes with the highest CPU usage on the system.

        This function iterates over all running processes, retrieves their CPU usage,
        and sorts them in descending order. The top K processes with the highest CPU
        usage are then selected and their details are returned as a string.

        Args:
            top_k (int): The number of top processes to return. Defaults to 6.

        Returns:
            str: A string representation of the top K processes with the highest CPU usage,
                 including their PID, name, user, status, creation time, CPU usage, and memory usage.
    """
    all_processes = list()
    for proc in psutil.process_iter():
        try:
            __proc = psutil.Process(proc.pid)
            all_processes.append((proc.pid, proc.cpu_percent(interval=0.1)))
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            pass
    all_processes.sort(key=lambda x: x[1], reverse=True)
    if len(all_processes) > top_k:
        all_processes = all_processes[:top_k]
    for i, _proc in enumerate(all_processes):
        try:
            process = psutil.Process(_proc[0])
            all_processes[i] = {
                'pid': _proc[0],
                'name': process.name(),
                'user': process.username(),
                'status': process.status(),
                'create_time': process.create_time(),
                'cpu_percent': _proc[1],
                'memory_percent': process.memory_percent()
            }
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            del all_processes[i]
    return str(all_processes)


def find_top_k_processes_with_the_highest_memory_usage(top_k: int = 6) -> str:
    """
        Finds the top K processes with the highest memory usage on the system.

        This function iterates over all running processes, retrieves their memory usage,
        and sorts them in descending order. The top K processes with the highest memory
        usage are then selected and their details are returned as a string.

        Args:
            top_k (int): The number of top processes to return. Defaults to 6.

        Returns:
            str: A string representation of the top K processes with the highest memory usage,
                 including their PID, name, user, status, creation time, CPU usage, and memory usage.
    """
    all_processes = list()
    for proc in psutil.process_iter():
        try:
            __proc = psutil.Process(proc.pid)
            all_processes.append((proc.pid, proc.memory_percent()))
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            pass
    all_processes.sort(key=lambda x: x[1], reverse=True)
    if len(all_processes) > top_k:
        all_processes = all_processes[:top_k]
    for i, _proc in enumerate(all_processes):
        try:
            process = psutil.Process(_proc[0])
            all_processes[i] = {
                'pid': _proc[0],
                'name': process.name(),
                'user': process.username(),
                'status': process.status(),
                'create_time': process.create_time(),
                'cpu_percent': process.cpu_percent(),
                'memory_percent': _proc[1]
            }
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            del all_processes[i]
    return str(all_processes)


def find_process_by_name(name: str) -> str:
    """
        Retrieves process information by name.

        Args:
            name (str): The name of the process to find.

        Returns:
            str: A string representation of the process info dictionary.
    """
    result = dict()
    for proc in psutil.process_iter(['name']):
        try:
            if proc.name() == name:
                result[proc.name()] = {
                    'pid': proc.pid,
                    'name': proc.name(),
                    'user': proc.username(),
                    'status': proc.status(),
                    'create_time': proc.create_time(),
                    'cpu_percent': proc.cpu_percent(interval=0.1),
                    'memory_percent': proc.memory_percent()
                }
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            pass
    return str(result)


def kill_a_process_by_pid(pid: int) -> bool:
    """
        Attempts to terminate a process by its Process ID (PID).

        This function terminates the specified process.
        If the process is successfully terminated, the function returns True. If the process
        does not exist or cannot be terminated, the function returns False.

        If you don't know very clear about the pid of the process you are going to kill, then kill pid=(-1), okay?

        Args:
            pid (int): The Process ID of the process to be terminated.

        Returns:
            bool: True if the process was terminated successfully, False otherwise.
    """
    if pid == 0 or pid == -1:
        return False
    try:
        process = psutil.Process(pid=pid)
        process.terminate()
        return True
    except (ValueError, TypeError, psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
        return False
