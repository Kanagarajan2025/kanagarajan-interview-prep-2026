# Day 1 — Linux Command Line Basics
**Date:** May 18, 2026 (your first day)  
**Goal:** Understand Linux well enough to confidently answer "How do you work on a Linux server?" in any interview.  
**This is the foundation of everything** — AWS runs on Linux, Docker runs on Linux, Kubernetes runs on Linux. If you skip this, everything else will be shaky.

---

## Your Detailed Timeline Today (End-to-End)

> **Total day:** 7:00 AM – 11:00 PM | Active study: ~14 hrs 45 min | Breaks: ~1 hr 15 min  
> Every block below includes **video / notes / practice / test time** broken down. Follow the order — it is designed so concepts build on each other.

---

### MORNING BLOCK — Theory (7:00 AM – 11:00 AM)

| Time | Block | What You Do | Breakdown |
|---|---|---|---|
| 7:00 – 7:30 AM | **Pre-Read** | Read this entire document top to bottom — no stopping, no practicing yet. Just absorb the structure. | Read: 25 min · Note unclear topics: 5 min |
| 7:30 – 8:35 AM | **VIDEO** | Watch **"Linux Commands for DevOps \| Linux Essentials for DevOps"** — Edureka (YouTube, ~1 hr 20 min). Link: https://www.youtube.com/watch?v=GzIFoJBVwh8 — Watch at **1.25× speed** (fits in ~64 min). Covers: What is Linux, Linux commands for DevOps, shell scripting basics, Git commands. Jot every command you see — do not pause to look anything up. | Watch: ~64 min |
| 8:30 – 9:00 AM | **Section 1** — What is Linux | Read your notes for this section. Then cover the page and answer out loud: *"Why do production servers run Linux and not Windows?"* | Read notes: 15 min · Self-quiz out loud: 10 min · Name 4 distros + their package managers: 5 min |
| 9:00 – 9:45 AM | **Section 2** — File System Structure | Read, then open Git Bash and run `ls /` — navigate into each major directory and do `ls`. Make it real. | Read notes: 15 min · Practice `ls /` navigation in Git Bash: 20 min · Mini-quiz (cover page, name 7 dirs + purpose): 10 min |
| 9:45 – 10:50 AM | **Section 3** — Essential Commands | Read once. Then run **every single command** in this section in Git Bash. No skipping. Type, not paste. | Read notes: 15 min · Practice all commands in Git Bash: 35 min · Mini-quiz (write `find` command from memory for .java files modified in last 7 days): 10 min |
| 10:50 – 11:00 AM | **Section 4** — Permissions (Part 1) | Read notes only — practice happens after lunch. | Read notes: 10 min |

---

### LUNCH BREAK (11:00 AM – 12:00 PM)

| Time | Activity |
|---|---|
| 11:00 AM – 12:00 PM | **Lunch + full break** — step away from screen. Your brain consolidates during rest. Mandatory. |

---

### AFTERNOON BLOCK — Theory Continued + DSA + Q&A (12:00 PM – 5:00 PM)

| Time | Block | What You Do | Breakdown |
|---|---|---|---|
| 12:00 – 12:35 PM | **Section 4** — Permissions (Part 2) | Continue from morning. Practice chmod then quiz. | Re-read key chmod table: 5 min · Practice: create 3 files, chmod 600 / 644 / 755, verify with `ls -la`: 20 min · Mini-quiz: what is 600? 644? 755? 777? Say it out loud: 10 min |
| 12:35 – 1:15 PM | **Section 5** — Process Management | Read, practice on your own running processes, quiz. | Read notes: 15 min · Practice: `ps aux`, `ps aux \| grep bash`, `lsof -i :8080`, `top` (q to exit): 15 min · Mini-quiz: how do you find and gracefully kill a Spring Boot process on port 8080?: 10 min |
| 1:15 – 2:00 PM | **Section 6** — Text Editors | Read, then actually open nano and vim — there is no other way to learn this. | Read notes: 10 min · Practice nano — open, write 3 lines, save (Ctrl+O + Enter), exit (Ctrl+X): 10 min · Practice vim — open, press `i`, type 3 lines, press Esc, type `:wq`: 15 min · Stress test — open same file in vim, change 1 line, then exit without saving (`:q!`), confirm nothing changed: 5 min · Mini-quiz: write 5 vim commands from memory: 5 min |
| 2:00 – 2:45 PM | **Section 7** — Piping + Text Processing | Read, then run all "real-world examples" on your `app.log` file (you create it in the practical block — create a sample version now). | Read notes: 10 min · Create a sample `app.log` with 8 lines (copy from Step 3 in Section 10): 5 min · Run all piping examples on your log: 20 min · Mini-quiz: write a one-liner from memory to find the top 3 most frequent errors: 10 min |
| 2:45 – 3:00 PM | **Rest** | Walk, hydrate. Re-watch any 5-minute segment of the Edureka video that felt unclear — at 1.5×. | 15 min |
| 3:00 – 4:00 PM | **DSA Block** — Two Sum (LeetCode #1) | Solve it yourself first. Read approach only if stuck at 30 min. Never copy code — write it. | Read problem: 5 min · Attempt brute force alone: 20 min · If stuck: read approach hint (Section 8 — not the code): 5 min · Write HashMap solution yourself: 15 min · Trace through example on paper: 10 min · Explain time/space complexity out loud: 5 min |
| 4:00 – 5:00 PM | **Interview Q&A** — Section 9 (7 questions) | For each question: read → write answer on paper → speak it out loud. Speaking is not optional. | 7 questions × 8–9 min each = 60 min total. **Q1:** chmod 755 · **Q2:** find + kill process · **Q3:** `>` vs `>>` · **Q4:** SIGTERM vs SIGKILL · **Q5:** /proc filesystem · **Q6:** which process uses port 8080 · **Q7:** nohup |

---

### EVENING BLOCK — Hands-On Practical (5:00 PM – 10:00 PM)

> **Rule:** Type every command. No copy-paste. Muscle memory is what you are building here.

| Time | Practical Block | What You Do | Goal |
|---|---|---|---|
| 5:00 – 5:20 PM | **Setup** | Install Git Bash (git-scm.com/download/win) — all defaults. Open it. | Git Bash running on your machine |
| 5:20 – 6:00 PM | **Practical 1** — First Commands | Run all commands in Section 10, Step 2. Create folder structure, navigate, verify with `pwd` and `ls`. | 40 min — you have a working project structure |
| 6:00 – 7:00 PM | **Practical 2** — File Operations | Section 10, Step 3. Create `application.properties`, `app.log`, practice `cat`, `grep`, `tail`, `head`. | 60 min — comfortable reading + creating files |
| 7:00 – 7:45 PM | **Practical 3** — Permissions | Section 10, Step 4. Write `deploy.sh`, chmod it, try running before and after chmod +x. | 45 min — you understand why execute permission matters |
| 7:45 – 9:00 PM | **Practical 4** — Processes + Search | Section 10, Step 5. `ps aux`, sort by memory, `find` with multiple flags. | 75 min — you can navigate any running system |
| 9:00 – 10:00 PM | **Practical 5** — Piping Challenges | Section 10, Step 6. Solve all 4 challenges yourself before looking at the solution. | 60 min — you can chain commands to solve real problems |

---

### END OF DAY (10:00 PM – 11:00 PM)

| Time | Activity | What to Do |
|---|---|---|
| 10:00 – 10:45 PM | **Write your notes** | Answer all 7 questions in Section 11 in your own words — not copied, not paraphrased from here. Your own sentences. |
| 10:45 – 11:00 PM | **Preview Day 2** | Read the Day 2 section in `30_Day_Study_Plan.md` so your brain primes overnight. |

---

### Time Summary

| Block | Time | Duration |
|---|---|---|
| Pre-read | 7:00 – 7:30 AM | 30 min |
| Video — Edureka Linux Commands for DevOps | 7:30 – 8:35 AM | **~64 min (1.25×)** |
| Section 1 (read + quiz) | 8:30 – 9:00 AM | 30 min |
| Section 2 (read + practice + quiz) | 9:00 – 9:45 AM | 45 min |
| Section 3 (read + practice + quiz) | 9:45 – 10:50 AM | 65 min |
| Section 4 Part 1 (read only) | 10:50 – 11:00 AM | 10 min |
| **Lunch Break** | 11:00 AM – 12:00 PM | **60 min** |
| Section 4 Part 2 (practice + quiz) | 12:00 – 12:35 PM | 35 min |
| Section 5 (read + practice + quiz) | 12:35 – 1:15 PM | 40 min |
| Section 6 (read + nano + vim + quiz) | 1:15 – 2:00 PM | 45 min |
| Section 7 (read + practice + quiz) | 2:00 – 2:45 PM | 45 min |
| **Rest** | 2:45 – 3:00 PM | **15 min** |
| DSA — Two Sum | 3:00 – 4:00 PM | 60 min |
| Interview Q&A (7 questions) | 4:00 – 5:00 PM | 60 min |
| Practical 1 — Setup + First Commands | 5:00 – 6:00 PM | 60 min |
| Practical 2 — File Operations | 6:00 – 7:00 PM | 60 min |
| Practical 3 — Permissions | 7:00 – 7:45 PM | 45 min |
| Practical 4 — Processes + Search | 7:45 – 9:00 PM | 75 min |
| Practical 5 — Piping Challenges | 9:00 – 10:00 PM | 60 min |
| Notes + Day 2 Preview | 10:00 – 11:00 PM | 60 min |
| **Total active study** | | **~14 hrs 45 min** |
| **Total breaks** | | **~1 hr 15 min** |

---

## Section 1 — What Is Linux and Why Does Every Server Run It?

> **How to study this section** | Time slot: **8:30 – 9:00 AM** | Total: 30 min  
> 1. **Read (15 min)** — Read the entire section below at normal speed.  
> 2. **Self-quiz (10 min)** — Cover the page. Answer out loud: *"Why do production servers run Linux and not Windows? Give 4 reasons."* Then uncover and check.  
> 3. **Spot-check (5 min)** — Without looking: name 4 Linux distributions and their package managers (`apt`, `yum`, etc.).

### The honest answer

Linux is an **operating system kernel** — the core software that sits between your hardware and your programs. It manages CPU time, memory, disk I/O, and network. Without a kernel, no program can run.

Linux was created by Linus Torvalds in 1991 as a free, open-source alternative to Unix. The code is public — anyone can read it, modify it, distribute it. That is why it dominates servers: it is free, stable, and has no licensing costs.

### Why servers don't run Windows

| Reason | What it means practically |
|---|---|
| **Cost** | Windows Server license costs money per core. Linux is free. At AWS scale, that is billions of dollars saved. |
| **Stability** | Linux servers run for years without rebooting. Windows often needs restarts for updates. |
| **Security** | Smaller attack surface. No GUI by default = fewer processes = fewer vulnerabilities. |
| **Performance** | Linux uses less RAM for the OS itself, leaving more for your application. |
| **Control** | Everything is a file. You can automate and script every aspect of the system. |
| **Docker/K8s** | All container technology is built on Linux kernel features (cgroups, namespaces). |

### Linux distributions (distros) you will encounter

- **Ubuntu** — most popular for development. `apt` package manager.
- **Amazon Linux 2023** — AWS's own Linux based on Red Hat. `yum` or `dnf` package manager. You will use this on EC2.
- **CentOS / Red Hat Enterprise Linux (RHEL)** — enterprise. `yum` package manager.
- **Alpine Linux** — tiny, used as Docker base images (5 MB vs Ubuntu's 70 MB).

**Interview tip:** If asked "which Linux have you used?" — say "Amazon Linux on EC2 for AWS workloads, and Ubuntu locally with Docker. I'm comfortable with both apt and yum."

---

## Section 2 — The Linux File System Structure

> **How to study this section** | Time slot: **9:00 – 9:45 AM** | Total: 45 min  
> 1. **Read (15 min)** — Study the directory tree and the table. Notice the pattern: config → `/etc`, logs → `/var/log`, programs → `/usr/bin`.  
> 2. **Practice in Git Bash (20 min)** — Run `ls /` to see real directories. `cd` into `/etc`, `/var`, `/tmp` and run `ls` inside each. Make it real.  
> 3. **Mini-quiz (10 min)** — Cover the page. Name 7 directories and what lives in each. Bonus: answer the interview question at the bottom of this section out loud.

This is the most disorienting thing for Windows users. Linux has **one tree** starting at `/`. There are no `C:\` or `D:\` drives. Everything — including USB drives and network shares — is mounted somewhere inside this single tree.

### The important directories and what lives there

```
/                    ← Root of everything. The top.
├── home/            ← User home directories
│   └── kanagarajan/ ← Your home directory. cd ~ takes you here.
├── root/            ← Home directory for the root (admin) user only
├── etc/             ← Configuration files for all programs
│   ├── nginx/       ← Nginx config lives here
│   ├── hosts        ← Local DNS overrides (like Windows hosts file)
│   └── environment  ← System-wide environment variables
├── var/             ← Variable data — things that change constantly
│   ├── log/         ← System logs: /var/log/syslog, /var/log/nginx/access.log
│   └── lib/         ← Application state (databases store data here)
├── tmp/             ← Temporary files. Cleared on reboot. Never store important things here.
├── usr/             ← User programs (installed software)
│   ├── bin/         ← Most commands you run live here: /usr/bin/python3, /usr/bin/java
│   └── local/       ← Software YOU installed (not via package manager)
├── bin/             ← Essential system commands needed before /usr is mounted
├── sbin/            ← System administration commands (only root can use most)
├── opt/             ← Optional software — some vendors install here (e.g. Datadog agent)
├── proc/            ← Virtual filesystem — represents running processes and kernel state
│   └── 1234/        ← A directory for process ID 1234 — contains its memory maps, etc.
├── sys/             ← Virtual filesystem — kernel and hardware information
├── dev/             ← Device files — /dev/sda is your hard disk, /dev/null is the void
└── mnt/             ← Mount point for external drives
```

### The most important things to remember

1. **`/etc`** = configuration. When a program behaves wrongly, check its config in `/etc`.
2. **`/var/log`** = logs. When something crashes, check logs here first.
3. **`/tmp`** = temporary. Safe to write here. Do not rely on it surviving a reboot.
4. **`~`** = your home directory shortcut. `cd ~` always takes you home.
5. **Everything is a file.** Your hard disk is `/dev/sda`. Your network socket is a file. The list of running processes is in `/proc`. This is the Unix philosophy.

### Interview question this covers

> **"What is the purpose of the /etc directory in Linux?"**  
> Answer: `/etc` contains system-wide configuration files for all installed programs. For example, `/etc/nginx/nginx.conf` configures Nginx, `/etc/hosts` overrides DNS lookups locally, and `/etc/environment` sets system-wide environment variables. It stands for "etcetera" historically but is now understood as the configuration home.

---

## Section 3 — Essential Commands (Learn These Cold)

> **How to study this section** | Time slot: **9:45 – 10:50 AM** | Total: 65 min  
> 1. **Read (15 min)** — Read all command groups: Navigation, File Operations, Reading, Searching, Creating.  
> 2. **Practice — type every command (35 min)** — Open Git Bash. Go through each group and run every single command. Do not copy-paste. If a command needs a file, create one first with `touch`. This is the most important 35 minutes of your morning.  
> 3. **Mini-quiz (10 min)** — Close this document. Write from memory: *(a)* the command to find all `.log` files modified in the last 7 days, *(b)* the difference between `cat` and `less`, *(c)* what `tail -f` does. Then re-open and check.

For each command: understand what it does, what the flags mean, and practice it tonight.

### Navigation

```bash
pwd                        # Print Working Directory — where am I right now?
ls                         # List files and folders in current directory
ls -l                      # Long format — shows permissions, owner, size, date
ls -la                     # Long format + hidden files (files starting with .)
ls -lh                     # Long format + human-readable sizes (KB, MB, GB)
cd /path/to/dir            # Change into a directory
cd ..                      # Go up one level
cd ~                       # Go to your home directory
cd -                       # Go back to previous directory (toggle)
```

**What `-l` output looks like and what each column means:**
```
-rwxr-xr-x  1  ec2-user  ec2-user  4096  May 15  deploy.sh
[1]         [2]  [3]        [4]      [5]   [6]      [7]

[1] Permissions (explained in Section 4)
[2] Number of hard links
[3] Owner (user)
[4] Group owner
[5] File size in bytes
[6] Last modified date
[7] File name
```

### File and Directory Operations

```bash
mkdir mydir                # Create a directory
mkdir -p a/b/c             # Create nested directories (parents too) — the -p flag
touch myfile.txt           # Create an empty file OR update its timestamp if it exists
cp source.txt dest.txt     # Copy a file
cp -r sourcedir/ destdir/  # Copy a directory and all contents (-r = recursive)
mv oldname.txt newname.txt # Rename a file
mv file.txt /tmp/          # Move a file to /tmp
rm file.txt                # Delete a file (PERMANENT — no recycle bin)
rm -r mydir/               # Delete a directory and all its contents
rm -rf mydir/              # Force delete without confirmation — BE VERY CAREFUL
```

**Important:** `rm -rf /` would delete everything on the system. Never run `rm -rf` without triple-checking the path.

### Reading File Contents

```bash
cat file.txt               # Print entire file to terminal
less file.txt              # Read file page by page (q to quit, /search to find text)
head file.txt              # Show first 10 lines
head -n 20 file.txt        # Show first 20 lines
tail file.txt              # Show last 10 lines
tail -f logfile.log        # Follow a log file in real time — new lines appear as written
                           # (Ctrl+C to stop) — you will use this constantly in DevOps
```

### Searching

```bash
grep "ERROR" app.log                     # Find all lines containing "ERROR"
grep -i "error" app.log                  # Case-insensitive search
grep -n "NullPointer" app.log            # Show line numbers
grep -r "database" /etc/                 # Search recursively inside /etc for "database"
grep -v "DEBUG" app.log                  # Show all lines that do NOT contain "DEBUG"
find / -name "*.java"                    # Find all .java files starting from root
find /home -name "*.log" -mtime -7       # Find .log files modified in last 7 days
find /tmp -type d                        # Find only directories inside /tmp
find . -name "*.conf" -exec cat {} \;    # Find .conf files and print their contents
```

### Creating and Writing Files

```bash
echo "Hello World"                       # Print text to terminal
echo "Hello World" > file.txt            # Write to file (OVERWRITES existing content)
echo "Second line" >> file.txt           # Append to file (adds to end, does not overwrite)
cat > file.txt                           # Type content, Ctrl+D to save
```

**Critical difference:** `>` overwrites. `>>` appends. Getting this wrong destroys data.

---

## Section 4 — File Permissions (Interviewers Love This)

> **How to study this section** | Time slot: **10:50 – 11:00 AM (read) → 12:00 – 12:35 PM (practice + quiz)** | Total: 45 min  
> 1. **Read (10 min before lunch)** — Read the permission string explanation and the chmod table. Just absorb — no practice yet.  
> 2. **Practice after lunch (20 min)** — In Git Bash: `touch file1 file2 file3`. Then: `chmod 600 file1`, `chmod 644 file2`, `chmod 755 file3`. Run `ls -la` after each. Read the permission string and mentally decode it.  
> 3. **Mini-quiz (10 min)** — Cover the page. Say out loud: what is `600`? `644`? `755`? `777`? Why must an SSH key be `600`? Then check.  
> 4. **Interview Q (5 min)** — Answer Q1 and Q2 from Section 9 out loud (you'll do the full Q&A block later — this is a preview).

This is one of the most tested Linux topics. Understand it deeply.

### How permissions work

Every file and directory has permissions for three categories of users:
- **Owner (u)** — the user who owns the file
- **Group (g)** — a group of users
- **Others (o)** — everyone else

Each category has three permission types:
- **Read (r)** — value: **4**
- **Write (w)** — value: **2**
- **Execute (x)** — value: **1**

### Reading the permission string

```
-rwxr-xr--
│├┤├─┤├─┤
│ │  │  └── Others: r-- = 4+0+0 = 4 (read only)
│ │  └───── Group:  r-x = 4+0+1 = 5 (read + execute)
│ └──────── Owner:  rwx = 4+2+1 = 7 (read + write + execute)
└────────── File type: - = regular file, d = directory, l = symbolic link
```

So `-rwxr-xr--` = **754** in numeric notation.

### The chmod command

```bash
chmod 755 deploy.sh        # Owner: rwx (7), Group: r-x (5), Others: r-x (5)
chmod 644 config.txt       # Owner: rw- (6), Group: r-- (4), Others: r-- (4)
chmod 600 my-key.pem       # Owner: rw- (6), Group: --- (0), Others: --- (0)
                           # Your SSH key MUST be 600 — SSH refuses to use keys that
                           # are readable by others (security measure)
chmod +x script.sh         # Add execute permission for all (symbolic notation)
chmod -x script.sh         # Remove execute permission for all
chmod u+x script.sh        # Add execute only for the owner
```

### Common permission patterns and why

| Permission | Numeric | Use case |
|---|---|---|
| `rwx------` | 700 | Private script — only owner can read/write/run |
| `rw-------` | 600 | SSH private key, sensitive config — must be this |
| `rwxr-xr-x` | 755 | Public script/binary — everyone can read and run |
| `rw-r--r--` | 644 | Public file — everyone reads, only owner writes |
| `rwxrwxrwx` | 777 | Everyone full access — almost never use this. Security risk. |

### The chown command

```bash
chown kanagarajan file.txt         # Change owner to kanagarajan
chown kanagarajan:developers file.txt  # Change owner AND group
chown -R kanagarajan:developers /app/  # Change owner recursively for all files inside /app
```

### Interview question this covers

> **"What does `chmod 755` mean?"**  
> Answer: `chmod 755` sets permissions to `rwxr-xr-x`. The owner (7 = read+write+execute) has full access. Group members (5 = read+execute) and all others (5 = read+execute) can read and run the file but cannot modify it. This is the standard permission for executable scripts or public binaries.

> **"Why must an SSH private key have permission 600?"**  
> Answer: The SSH client (`ssh` command) refuses to use a private key file if it is readable by anyone other than the owner. This is a deliberate security check — if your key file has `644` or `755`, SSH will print "Permissions are too open" and refuse to connect. `600` (rw-------) ensures only you can read it.

---

## Section 5 — Process Management

> **How to study this section** | Time slot: **12:35 – 1:15 PM** | Total: 40 min  
> 1. **Read (15 min)** — Read all command groups: viewing, understanding `ps aux` output, killing, background processes, port checking.  
> 2. **Practice (15 min)** — In Git Bash: run `ps aux` (you'll see your Git Bash processes). Run `ps aux | grep bash`. Run `ps aux --sort=-%mem | head -5`. Run `lsof -i :8080` (nothing will show if no server is running — that's fine, note the output format). Run `top` and press `q` to quit.  
> 3. **Mini-quiz (10 min)** — Cover the page. Answer out loud: *"A Java app is stuck and not responding. Walk me through how you would find it and shut it down — both gracefully and forcefully."*

When your Spring Boot app is running on a server, it is a **process**. You need to find it, monitor it, and sometimes kill it.

### Viewing processes

```bash
ps                         # Show processes owned by current user in this terminal session
ps aux                     # Show ALL processes from ALL users (a=all users, u=user format, x=background processes)
ps aux | grep java         # Find the Java process specifically — you'll use this constantly
top                        # Real-time view of all processes — CPU%, Memory%, updated every 3s
                           # Press q to quit, k to kill a process, M to sort by memory, P to sort by CPU
htop                       # Better version of top — install with: sudo yum install htop -y
```

### Understanding `ps aux` output

```
USER    PID  %CPU %MEM   VSZ  RSS  STAT  START  TIME  COMMAND
root      1   0.0  0.1  4196 1060  Ss    05:00  0:01  /sbin/init
ec2-user 1234 25.0  8.5 2048000 173056  Sl  09:15  2:30  java -jar app.jar

PID    = Process ID — unique number for this process. Use this to kill it.
%CPU   = CPU usage at this moment
%MEM   = RAM usage as % of total RAM
VSZ    = Virtual memory size (total address space)
RSS    = Resident Set Size — actual RAM in use (use this for real memory usage)
STAT   = Process state: S=sleeping, R=running, Z=zombie (parent not cleaned up), D=disk wait
COMMAND = The actual command that started the process
```

### Killing processes

```bash
kill 1234                  # Send SIGTERM (15) to process 1234 — asks it to shut down gracefully
kill -9 1234               # Send SIGKILL (9) — force kill immediately, no cleanup possible
kill -15 1234              # Same as kill 1234 — graceful shutdown
killall java               # Kill ALL processes named "java"
pkill -f "app.jar"         # Kill all processes whose command line contains "app.jar"
```

**SIGTERM vs SIGKILL:** Always try SIGTERM first. It gives the app time to close DB connections, flush buffers, and clean up. SIGKILL is instant death — connection pools leak, in-flight requests drop. In a Spring Boot context, a graceful shutdown (SIGTERM) lets `@PreDestroy` methods run.

### Background processes

```bash
java -jar app.jar &            # The & runs the process in the background — terminal stays free
nohup java -jar app.jar &      # nohup = "no hangup" — process keeps running even if you close
                               # the SSH session. Output goes to nohup.out by default.
nohup java -jar app.jar > app.log 2>&1 &   # Redirect all output to app.log
                                           # 2>&1 = redirect stderr (2) to wherever stdout (1) goes
jobs                       # List background jobs in current session
fg %1                      # Bring job 1 back to foreground
bg %1                      # Resume a stopped job in background
```

### Checking what's using a port

```bash
lsof -i :8080              # List open files on port 8080 — shows which process is using it
netstat -tlnp              # Show all listening ports and which process owns them
ss -tlnp                   # Modern replacement for netstat (faster, same info)
```

**When you'll use this:** Your Spring Boot app fails to start with "Port 8080 already in use" — run `lsof -i :8080` to find which process is using it, then kill it.

---

## Section 6 — Text Editors: nano and vim

> **How to study this section** | Time slot: **1:15 – 2:00 PM** | Total: 45 min  
> 1. **Read (10 min)** — Read the nano controls and the vim survival kit.  
> 2. **Practice nano (10 min)** — In Git Bash: `nano test.txt`. Type 3 lines. Press `Ctrl+O`, then Enter to save. Press `Ctrl+X` to exit. Run `cat test.txt` to verify.  
> 3. **Practice vim (15 min)** — `vim test2.txt`. Press `i`. Type 3 lines. Press `Esc`. Type `:wq`. Run `cat test2.txt`. Now open it again with `vim test2.txt`, press `i`, add a 4th line, press `Esc`, type `:q!` to exit without saving. Run `cat test2.txt` — the 4th line should NOT be there.  
> 4. **Stress test (5 min)** — Open a file in vim. Make changes. Deliberately use `:q` (not `:wq`). Vim will warn you. Learn what the warning looks like.  
> 5. **Mini-quiz (5 min)** — Without looking: write the vim commands for save, quit, force-quit, delete a line, go to last line, search for a word.

You will need to edit files on a server. There is no VS Code on a production server — only terminal editors.

### nano — use this first (beginner friendly)

```bash
nano filename.txt          # Open or create a file in nano
```

**Controls inside nano:**
- Type normally to write
- `Ctrl+O` then Enter = Save (Write Out)
- `Ctrl+X` = Exit
- `Ctrl+K` = Cut current line
- `Ctrl+U` = Paste
- `Ctrl+W` = Search (Where is)

### vim — you must know the basics (it is everywhere)

Vim has **modes**. This is what confuses beginners:
- **Normal mode** (default) — every key is a command. `j` moves down, `d` deletes.
- **Insert mode** — you can type text normally.
- **Command mode** — run commands with `:`.

```bash
vim filename.txt           # Open a file in vim
```

**The essential vim survival kit:**

```
i          Enter insert mode (now you can type)
Esc        Return to normal mode (press this whenever confused)
:w         Save (write) the file
:q         Quit (only works if no unsaved changes)
:wq        Save and quit
:q!        Quit without saving — force quit (use this when you panic)
:wq!       Force save and quit

In Normal mode:
dd         Delete (cut) the current line
yy         Yank (copy) the current line
p          Paste
/search    Search for "search" — n jumps to next match
u          Undo
Ctrl+R     Redo
gg         Go to first line
G          Go to last line
:10        Go to line 10
```

**The minimum you need:** Open with `vim file`, press `i` to type, press `Esc` when done, type `:wq` to save and exit. That is enough for 90% of server situations.

---

## Section 7 — Piping, Redirection, and Text Processing

> **How to study this section** | Time slot: **2:00 – 2:45 PM** | Total: 45 min  
> 1. **Read (10 min)** — Read piping, redirection, and the text processing commands table.  
> 2. **Practice on app.log (20 min)** — Create the sample `app.log` from Section 10 Step 3 now (just the echo lines). Then run all 4 real-world examples from the "Real-world examples you would use at work" block. Type each one — understand what each `|` is doing.  
> 3. **Mini-quiz (10 min)** — Without looking, write: *(a)* a command to count ERROR lines in a log, *(b)* a command to find the top 5 most frequent errors with their count, *(c)* the difference between `>` and `>>`. Say the answers out loud.  
> 4. **Bonus challenge (5 min)** — Use `sed -i` to replace `localhost:3306` with `prod-db:3306` in your `application.properties`. Verify with `cat`.

This is where Linux becomes extremely powerful. You chain simple commands together to do complex things.

### Piping — `|`

The pipe `|` takes the **output of the left command** and sends it as **input to the right command**.

```bash
cat app.log | grep "ERROR"                   # Read log, filter for ERROR lines only
cat app.log | grep "ERROR" | wc -l          # Count how many ERROR lines
ps aux | grep java                           # Find Java processes
ls -la | sort -k5 -n                         # List files, sort by size (column 5)
cat /etc/passwd | cut -d: -f1               # Get all usernames from passwd file
```

### Redirection — `>` and `>>`

```bash
command > file.txt          # Send output to file (OVERWRITES)
command >> file.txt         # Append output to file
command 2> error.log        # Send STDERR (error output) to error.log
command 2>&1                # Merge stderr into stdout
command > output.log 2>&1   # Send BOTH stdout and stderr to output.log
command < input.txt         # Read input FROM a file instead of keyboard
```

### Useful text processing commands

```bash
wc -l file.txt              # Word Count — count lines in a file
wc -w file.txt              # Count words
sort file.txt               # Sort lines alphabetically
sort -n numbers.txt         # Sort numerically
sort -r file.txt            # Sort in reverse
uniq file.txt               # Remove consecutive duplicate lines
sort file.txt | uniq -c     # Count occurrences of each unique line
cut -d',' -f2 data.csv      # Extract column 2 from CSV (-d = delimiter, -f = field)
awk '{print $1}' file.txt   # Print first column (space-delimited)
sed 's/old/new/g' file.txt  # Replace all occurrences of "old" with "new"
```

### Real-world examples you would use at work

```bash
# Find all ERROR lines in last 100 lines of log, count them
tail -100 app.log | grep "ERROR" | wc -l

# Find the top 10 most common errors
grep "ERROR" app.log | sort | uniq -c | sort -rn | head -10

# Find all Java processes and their PIDs
ps aux | grep java | grep -v grep | awk '{print $2, $11}'

# Replace the database URL in a config file
sed -i 's/localhost:3306/prod-db.example.com:3306/g' application.properties
# -i = in-place (edit the file, don't just print to terminal)
```

---

## Section 8 — DSA Block: Two Sum (3:00 PM – 4:00 PM)

**Platform:** LeetCode Problem #1 — Two Sum  
**Time limit for yourself:** 30 minutes to solve. If stuck at 30 min, read the approach below. Never copy — write the code yourself.

### The Problem

Given an array of integers `nums` and a target integer `target`, return the **indices** of the two numbers that add up to `target`. Exactly one solution exists. Cannot use the same element twice.

**Example:**
```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Reason: nums[0] + nums[1] = 2 + 7 = 9
```

### Step 1 — Brute Force (write this first, always)

Check every pair:

```java
public int[] twoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return new int[]{i, j};
            }
        }
    }
    return new int[]{};
}
```

**Time complexity:** O(n²) — for each element, we check all remaining elements  
**Space complexity:** O(1) — no extra memory

### Step 2 — Optimal Solution (HashMap)

**The insight:** For every number `x`, we need `target - x`. Instead of searching the whole array every time, store what we've seen so far in a HashMap.

```java
public int[] twoSum(int[] nums, int target) {
    // key = number value, value = its index
    Map<Integer, Integer> seen = new HashMap<>();
    
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];   // What number do we need?
        
        if (seen.containsKey(complement)) {  // Have we seen it before?
            return new int[]{seen.get(complement), i};  // Return both indices
        }
        
        seen.put(nums[i], i);  // Store current number and its index
    }
    
    return new int[]{};  // No solution found (problem guarantees this won't happen)
}
```

**Time complexity:** O(n) — one pass through the array  
**Space complexity:** O(n) — HashMap stores at most n elements

### Trace through the example

```
nums = [2, 7, 11, 15], target = 9

i=0: complement = 9-2 = 7. seen is empty. seen = {2:0}
i=1: complement = 9-7 = 2. seen has 2! Return [seen.get(2), 1] = [0, 1]. ✓
```

### What the interviewer is testing

1. Can you write a correct brute force?
2. Do you recognize the HashMap pattern for O(1) lookup?
3. Can you explain time/space complexity?
4. Do you trace through an example to verify?

### What to say out loud during the interview

> "I'll start with the brute force — nested loops, check every pair, O(n²) time. That works. But we can do better. For each number, I need to find its complement — the difference between the target and the current number. If I store numbers I've already seen in a HashMap, I can check for the complement in O(1) instead of O(n). So one pass through the array, O(n) time, O(n) space. Let me code that."

---

## Section 9 — Interview Q&A (4:00 PM – 5:00 PM)

**Instructions:** Read the question. Close this document. Write your answer on paper. Then come back and compare. Then say your answer OUT LOUD. The speaking part is not optional — interviews are verbal.

---

**Q1: What does `chmod 755` mean?**

Full answer:
> `chmod 755` sets the file permission to `rwxr-xr-x`. The first digit `7` applies to the owner: read (4) + write (2) + execute (1) = 7, so the owner has full access. The second digit `5` applies to the group: read (4) + execute (1) = 5, no write access. The third digit `5` applies to all others: same as group. This is the standard permission for executable scripts — the owner can modify and run it, everyone else can only read and run it.

---

**Q2: How do you find a running process and kill it in Linux?**

Full answer:
> I use `ps aux | grep java` to find the process — this shows all running processes filtered to ones with "java" in their command. The output shows the PID (process ID) in the second column. Then I use `kill <PID>` to send a graceful shutdown signal (SIGTERM), which gives the application time to clean up — close database connections, complete in-flight requests. If the process doesn't respond to SIGTERM within a reasonable time, I use `kill -9 <PID>` to force-kill it immediately, though this risks leaving resources in an inconsistent state. I'd use `kill -9` only as a last resort.

---

**Q3: What is the difference between `>` and `>>` in Linux?**

Full answer:
> `>` redirects the output of a command to a file and **overwrites** the file completely if it exists. For example, `echo "new" > file.txt` replaces everything in `file.txt`. `>>` **appends** the output to the end of the file without removing existing content. In a DevOps context, when I'm writing logs or collecting command output, I always use `>>` to avoid accidentally destroying data from previous runs — for example, `mvn test >> build.log 2>&1` appends test results to the log rather than overwriting it.

---

**Q4: What is the difference between SIGTERM and SIGKILL?**

Full answer:
> SIGTERM (signal 15) is a polite request for the process to terminate. The process receives the signal and can handle it — finishing current work, closing files, releasing locks, running cleanup code like `@PreDestroy` methods in Spring. SIGKILL (signal 9) cannot be caught or ignored by the process — the kernel immediately terminates it with no warning. This means open files may be left in a corrupt state, database connections leak back to the connection pool, and any in-flight requests are abruptly dropped. I always use SIGTERM first and only escalate to SIGKILL if the process is genuinely hung.

---

**Q5: What is the `/proc` filesystem?**

Full answer:
> `/proc` is a virtual filesystem — it doesn't correspond to real files on disk. It is generated by the kernel on the fly to expose information about running processes and kernel state. For example, `/proc/1234/` is a directory containing information about the process with PID 1234 — its memory maps, open file descriptors, environment variables, and command line. `/proc/cpuinfo` shows CPU details, `/proc/meminfo` shows memory usage. This is how tools like `top` and `ps` get their data — they read from `/proc`. This is also the Unix "everything is a file" philosophy in practice.

---

**Q6: How do you check which process is using port 8080?**

Full answer:
> I use `lsof -i :8080` — lsof stands for "list open files" and since network sockets are files in Linux, it shows which process has port 8080 open. The output includes the process name, PID, and user. Alternatively, `ss -tlnp | grep 8080` or `netstat -tlnp | grep 8080` gives the same result — `ss` is the modern replacement for `netstat`. Once I have the PID, I can kill it or investigate further with `ps aux | grep <PID>`.

---

**Q7: What is `nohup` and why would you use it?**

Full answer:
> `nohup` stands for "no hangup". By default, when you close an SSH session, the terminal sends a SIGHUP signal to all processes that were started in it, causing them to terminate. `nohup java -jar app.jar &` prevents this — the process keeps running even after you disconnect. The `&` at the end puts it in the background so your terminal prompt returns immediately. Output that would normally go to the terminal is redirected to `nohup.out` by default. For production, I'd use `systemctl` to manage services properly — but `nohup` is useful for quick testing on a server.

---

## Section 10 — Practical Block (5:00 PM – 10:00 PM)

### Step 1: Install Git Bash (5:00 PM – 5:20 PM)

1. Go to: https://git-scm.com/download/win
2. Download and install with all defaults
3. Right-click on desktop → "Git Bash Here"
4. You now have a Linux terminal on Windows

### Step 2: Verify and run first commands (5:20 PM – 6:00 PM)

Open Git Bash and type every command below. Do NOT copy-paste. Type each one:

```bash
# Where am I?
pwd

# What's in my home directory?
ls -la

# What Linux are we faking here?
uname -a

# Create your project structure
mkdir -p ~/projects/myapp/src/main/java
mkdir -p ~/projects/myapp/src/main/resources
mkdir -p ~/projects/myapp/src/test

# Navigate and verify
cd ~/projects
ls -la
cd myapp
pwd
```

### Step 3: File operations practice (6:00 PM – 7:00 PM)

```bash
# Create a simulated application.properties file
cd ~/projects/myapp/src/main/resources
echo "server.port=8080" > application.properties
echo "spring.datasource.url=jdbc:mysql://localhost:3306/mydb" >> application.properties
echo "spring.datasource.username=admin" >> application.properties
echo "spring.datasource.password=secret123" >> application.properties
echo "spring.redis.host=localhost" >> application.properties
echo "spring.redis.port=6379" >> application.properties

# Read the file
cat application.properties

# Search inside it
grep "datasource" application.properties
grep "port" application.properties

# Simulate a log file
cd ~/projects/myapp
echo "[INFO]  2026-05-17 09:00:01 Application started on port 8080" > app.log
echo "[INFO]  2026-05-17 09:00:15 User U001 logged in" >> app.log
echo "[ERROR] 2026-05-17 09:01:02 NullPointerException in BookingService.java:142" >> app.log
echo "[INFO]  2026-05-17 09:01:30 User U002 logged in" >> app.log
echo "[WARN]  2026-05-17 09:02:00 Redis connection slow: 250ms" >> app.log
echo "[ERROR] 2026-05-17 09:03:45 Database connection timeout after 30s" >> app.log
echo "[INFO]  2026-05-17 09:04:00 User U003 booked flight AK-123" >> app.log
echo "[ERROR] 2026-05-17 09:05:12 OutOfMemoryError in PaymentService" >> app.log

# Count ERROR lines
grep "ERROR" app.log | wc -l

# Show only ERROR lines
grep "ERROR" app.log

# Find top errors
grep "ERROR" app.log | sort | uniq -c | sort -rn

# Show last 3 log lines
tail -3 app.log

# Show first 2 log lines
head -2 app.log
```

### Step 4: Permissions practice (7:00 PM – 7:45 PM)

```bash
# Create a deployment script
cd ~/projects/myapp
cat > deploy.sh << 'EOF'
#!/bin/bash
echo "Starting deployment..."
echo "Stopping old process..."
pkill -f "app.jar" 2>/dev/null || true
echo "Starting new version..."
nohup java -jar app.jar > app.log 2>&1 &
echo "Deployment complete. PID: $!"
EOF

# Check its default permissions
ls -la deploy.sh

# Try to run it (will fail — not executable yet)
./deploy.sh

# Make it executable
chmod +x deploy.sh

# Run it (will fail because java -jar app.jar won't work, but the script runs)
./deploy.sh

# Verify the permission change
ls -la deploy.sh

# Practice different permissions
touch secretfile.txt
chmod 600 secretfile.txt
ls -la secretfile.txt   # Should show -rw-------

touch publicfile.txt
chmod 644 publicfile.txt
ls -la publicfile.txt   # Should show -rw-r--r--
```

### Step 5: Process and search practice (7:45 PM – 9:00 PM)

```bash
# View running processes
ps aux

# Find bash processes
ps aux | grep bash

# How many processes are running?
ps aux | wc -l

# Find the largest processes by memory
ps aux --sort=-%mem | head -10

# Practice find command
find ~/projects -name "*.txt"
find ~/projects -name "*.sh"
find ~/projects -type d              # Find only directories
find ~/projects -name "*.log" -size +0c   # Find non-empty log files

# Practice grep with the log file
grep -n "ERROR" ~/projects/myapp/app.log    # With line numbers
grep -c "INFO" ~/projects/myapp/app.log     # Count matching lines
grep -v "INFO" ~/projects/myapp/app.log     # Lines WITHOUT INFO
```

### Step 6: Piping challenge (9:00 PM – 10:00 PM)

Write the commands yourself (answers below — check only after trying):

**Challenge 1:** Find all log entries that are either ERROR or WARN, and count them.
```bash
# Your answer here first...

# Solution:
grep -E "ERROR|WARN" ~/projects/myapp/app.log | wc -l
```

**Challenge 2:** Show only the timestamp part (first 2 "words") of each log line.
```bash
# Your answer here first...

# Solution:
cat ~/projects/myapp/app.log | awk '{print $1, $2}'
```

**Challenge 3:** Find the log level (INFO/WARN/ERROR) from each line and count how many of each.
```bash
# Your answer here first...

# Solution:
grep -o "\[.*\]" ~/projects/myapp/app.log | sort | uniq -c
```

**Challenge 4:** Simulate watching a live log file (open two Git Bash windows):
```bash
# Terminal 1: Watch the log
tail -f ~/projects/myapp/app.log

# Terminal 2: Add new entries
echo "[INFO]  2026-05-17 10:00:00 New entry added" >> ~/projects/myapp/app.log
echo "[ERROR] 2026-05-17 10:00:01 Payment failed for user U004" >> ~/projects/myapp/app.log
```
Watch the new lines appear instantly in Terminal 1.

---

## Section 11 — End of Day Notes (10:00 PM – 11:00 PM)

### What to write in your notes (your own words — not copy from here)

Write answers to these in a notebook or Notion:

1. What is Linux and why do servers use it? (3 sentences max)
2. What are the 5 most important directories and what is in each?
3. What is the difference between `>` and `>>`?
4. What does `chmod 755` mean?
5. How do you find a process and kill it gracefully?
6. What is the difference between SIGTERM and SIGKILL?
7. Draw the permission bit structure: `rwxr-xr--` explained

### Tomorrow preview (Day 2)

Day 2 covers:
- SSH — how public/private key authentication works (you'll actually generate keys and understand what each file is)
- `curl` and `wget` — make HTTP calls from terminal (you'll test APIs without Postman)
- `systemctl` — manage services
- Environment variables — `$PATH`, `.bashrc`
- Package managers: `apt` and `yum`

**What to install tonight before sleeping:**
Nothing. Git Bash is enough for Day 2.

---

## Quick Reference Card (Tear-Out)

```
NAVIGATION          SEARCH              PERMISSIONS
pwd                 grep "text" file    chmod 755 file
ls -la              grep -r "text" dir  chmod +x file
cd ~                find / -name "*.x"  chmod 600 key.pem
cd ..               grep -n = line nums chown user file

FILES               PROCESSES           REDIRECTION
touch file          ps aux              cmd > file (overwrite)
cat file            ps aux | grep java  cmd >> file (append)
less file           kill PID            cmd 2>&1 (merge stderr)
tail -f file        kill -9 PID         cmd | other (pipe)
head -n 20 file     lsof -i :8080

TEXT PROCESSING
wc -l file          = count lines
sort file           = sort alphabetically
uniq -c             = count unique
awk '{print $2}'    = print column 2
sed 's/old/new/g'   = replace text
```

---

**Day 1 complete when:**
- [ ] You can navigate the Linux file system without looking at this doc
- [ ] You can create files, write to them, append to them, read them
- [ ] You understand `chmod 755` and can explain it in an interview
- [ ] You can find a process by name and kill it gracefully
- [ ] You solved Two Sum with the HashMap approach and can explain why it is O(n)
- [ ] You can answer all 7 interview questions out loud without reading notes
- [ ] Your notes are written in your own words
