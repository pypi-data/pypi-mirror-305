import os
import subprocess

class Audio:
    def __init__(self, computer):
        self.computer = computer

    def transcribe(self, audio_path, display=True):
        # Define the directory to store the model
        model_dir = os.path.expanduser('~/models')
        os.makedirs(model_dir, exist_ok=True)
        
        # Define the model file path
        model_path = os.path.join(model_dir, 'whisper-tiny.en.llamafile')
        
        # Download the model if it doesn't exist
        if not os.path.exists(model_path):
            # Try different download methods across platforms
            download_success = False
            download_url = 'https://huggingface.co/Mozilla/whisperfile/resolve/main/whisper-tiny.en.llamafile'
            
            def try_download_with_python():
                try:
                    import urllib.request
                    urllib.request.urlretrieve(download_url, model_path)
                    return True
                except Exception:
                    return False
            
            # Try platform-specific methods first
            if os.name == 'nt':  # Windows
                try:
                    # Try powershell first
                    ps_command = f'Invoke-WebRequest -Uri "{download_url}" -OutFile "{model_path}"'
                    subprocess.run(['powershell', '-Command', ps_command], check=True)
                    download_success = True
                except Exception:
                    # Try curl (included in recent Windows versions)
                    try:
                        subprocess.run(['curl', '-L', '-o', model_path, download_url], check=True)
                        download_success = True
                    except Exception:
                        download_success = try_download_with_python()
            
            else:  # macOS or Linux
                # Try curl first (pre-installed on macOS)
                try:
                    subprocess.run(['curl', '-L', '-o', model_path, download_url], check=True)
                    download_success = True
                except (subprocess.CalledProcessError, FileNotFoundError):
                    # Try wget
                    try:
                        subprocess.run(['wget', '-O', model_path, download_url], check=True)
                        download_success = True
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        # If wget/curl failed, try to install them
                        if sys.platform == 'darwin':  # macOS
                            try:
                                # Try installing wget via homebrew
                                subprocess.run(['brew', 'install', 'wget'], check=True)
                                subprocess.run(['wget', '-O', model_path, download_url], check=True)
                                download_success = True
                            except Exception:
                                download_success = try_download_with_python()
                        else:  # Linux
                            try:
                                # Try apt-get (Debian/Ubuntu)
                                subprocess.run(['sudo', 'apt-get', 'update'], check=True)
                                subprocess.run(['sudo', 'apt-get', 'install', '-y', 'wget'], check=True)
                                subprocess.run(['wget', '-O', model_path, download_url], check=True)
                                download_success = True
                            except Exception:
                                try:
                                    # Try yum (CentOS/RHEL)
                                    subprocess.run(['sudo', 'yum', 'install', '-y', 'wget'], check=True)
                                    subprocess.run(['wget', '-O', model_path, download_url], check=True)
                                    download_success = True
                                except Exception:
                                    try:
                                        # Try pacman (Arch Linux)
                                        subprocess.run(['sudo', 'pacman', '-Sy', 'wget', '--noconfirm'], check=True)
                                        subprocess.run(['wget', '-O', model_path, download_url], check=True)
                                        download_success = True
                                    except Exception:
                                        download_success = try_download_with_python()
            
            if not download_success:
                raise RuntimeError("Failed to download model file. Please ensure you have internet access and try again.")
        
        # Make the file executable
        subprocess.run(['chmod', '+x', model_path], check=True)

        command = f"{model_path} -f {audio_path} --no-prints"
        
        # Run the transcription
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            shell=True,
            # executable='/bin/bash'  # Specify the shell explicitly
        )
        
        full_output = ""
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                if display:
                    print(output.strip())
                full_output += output

        return_code = process.poll()
        
        if return_code == 0:
            return full_output
        else:
            error_output = process.stderr.read()
            return f"Transcription failed with return code {return_code}: {error_output}"