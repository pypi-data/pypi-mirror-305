import time
from typing import Dict, Any, Optional, Union

class ProductivityTimer:
    """
    A class for managing multiple timers, one for each specified person.
    Provides functions to start, stop, pause, resume, reset, and check elapsed time for each timer.
    
    Attributes:
        timers (dict): A dictionary storing each person's timer details. Each key is a person's name, and the value is a dictionary containing:
            - 'start_time' (float): The time when the timer started.
            - 'elapsed_time' (float): The total elapsed time for the timer.
            - 'running' (bool): Indicates whether the timer is currently running.
            - 'timeout' (float or None): The maximum allowed time in seconds for the timer; None means no timeout.
    """
    
    def __init__(self)-> None:

        """Initializes the ProductivityTimer with an empty dictionary for timers."""
        self.timers = {}

    def start(self, person: str, timeout: Optional[float] = None) -> None:
        """
        Starts or restarts a timer for a specified person.
        
        Args:
            person (str): The name of the person for whom the timer is started.
            timeout (float, optional): The maximum allowed time in seconds; timer stops automatically when exceeded. Default is None.
        """
        if person not in self.timers:
            self.timers[person] = {'start_time': None, 'elapsed_time': 0, 'running': False, 'timeout': timeout}
        
        if not self.timers[person]['running']:
            self.timers[person]['start_time'] = time.time()
            self.timers[person]['running'] = True
            print(f"Timer started for {person}." + (f" Timeout: {timeout} seconds." if timeout else ""))
        else:
            print(f"Timer for {person} is already running.")

    def resume(self, person: str) -> None:
        """
        Resumes a paused timer for the specified person.
        
        Args:
            person (str): The name of the person for whom the timer is resumed.
        """
        if person in self.timers and not self.timers[person]['running']:
            self.timers[person]['start_time'] = time.time()
            self.timers[person]['running'] = True
            print(f"Timer resumed for {person}.")
        elif person not in self.timers:
            print(f"No timer found for {person} to resume.")
        else:
            print(f"Timer for {person} is already running.")

    def stop(self, person: str) -> None:
        """
        Stops the timer for a specified person, updating their elapsed time.
        
        Args:
            person (str): The name of the person for whom the timer is stopped.
        """
        if person in self.timers and self.timers[person]['running']:
            self.timers[person]['elapsed_time'] += time.time() - self.timers[person]['start_time']
            self.timers[person]['running'] = False
            print(f"Timer stopped for {person}.")
        elif person not in self.timers:
            print(f"No timer found for {person} to stop.")
        else:
            print(f"Timer for {person} is already stopped.")

    def reset(self, person: str) -> None:
        """
        Resets the timer for a specified person.
        
        Args:
            person (str): The name of the person for whom the timer is reset.
        """
        if person in self.timers:
            self.timers[person] = {'start_time': None, 'elapsed_time': 0, 'running': False, 'timeout': self.timers[person].get('timeout')}
            print(f"Timer reset for {person}.")
        else:
            print(f"No timer found for {person} to reset.")

    def pause(self, person: str) -> None:
        """
        Pauses the timer for a specified person without resetting their elapsed time.
        
        Args:
            person (str): The name of the person for whom the timer is paused.
        """
        if person in self.timers and self.timers[person]['running']:
            self.stop(person)
            print(f"Timer paused for {person}.")
        elif person not in self.timers:
            print(f"No timer found for {person} to pause.")

    def get_elapsed_time(self, person: str, formatted: bool = False) -> Union[float, str]:
        """
        Retrieves the elapsed time for a specified person.
        
        Args:
            person (str): The name of the person for whom the elapsed time is retrieved.
            formatted (bool, optional): If True, returns elapsed time as a formatted string in H:M:S format. Default is False.
        
        Returns:
            float or str: The elapsed time in seconds or as a formatted string in H:M:S format.
        """
        if person in self.timers:
            timer = self.timers[person]
            elapsed = timer['elapsed_time'] + (time.time() - timer['start_time']) if timer['running'] else timer['elapsed_time']
            if formatted:
                return time.strftime("%H:%M:%S", time.gmtime(elapsed))
            return elapsed
        print(f"No timer found for {person}.")
        return 0.0

    def get_all_elapsed_times(self, formatted: bool = False) -> Dict[str, Union[float, str]]:
        """
        Returns a dictionary with the elapsed times for all tracked persons.
        
        Args:
            formatted (bool, optional): If True, returns elapsed times as formatted strings in H:M:S format. Default is False.
        
        Returns:
            dict: A dictionary with elapsed times for all persons.
        """
        return {person: self.get_elapsed_time(person, formatted) for person in self.timers}

    def stop_all(self) -> None:
        """Stops all active timers and updates their elapsed times."""
        for person in self.timers:
            if self.timers[person]['running']:
                self.stop(person)
        print("All timers stopped.")

    def reset_all(self) -> None:
        """Resets all timers to their initial state."""
        for person in self.timers:
            self.reset(person)
        print("All timers reset.")

    def active_timers(self) -> list[str]:
        """
        Returns a list of persons with active timers.
        
        Returns:
            list: A list of persons with currently active timers.
        """
        return [person for person, timer in self.timers.items() if timer['running']]

    def check_timeouts(self) -> None:
        """Checks if any timers have exceeded their timeouts and stops them if so."""
        for person, timer in self.timers.items():
            if timer['timeout'] and timer['running']:
                elapsed = self.get_elapsed_time(person)
                if elapsed >= timer['timeout']:
                    self.stop(person)
                    print(f"Timer for {person} has reached its timeout of {timer['timeout']} seconds and was stopped.")

    def __str__(self) -> str:
        """
        Returns a summary of elapsed times for all tracked persons in a readable format.
        
        Returns:
            str: A summary of elapsed times in H:M:S format for each person.
        """
        summary = "Elapsed times:\n"
        for person, elapsed_time in self.get_all_elapsed_times(formatted=True).items():
            summary += f"{person}: {elapsed_time}\n"
        return summary
