
# 1 worker
# visitor 5000
# 6 concurrent users (active user)
# 25 users (login user)


light_worker_ratio = 0.8  # 80% are lighter workers
heavy_worker_ratio = 0.2  # 20% are heavier workers
light_worker_ram_estimation = 150  # MB
heavy_worker_ram_estimation = 1024  # MB (1 GB)

# Define the number of workers
num_workers = 2

# Calculate memory limits
limit_memory_hard = num_workers * ((light_worker_ratio * light_worker_ram_estimation) + (heavy_worker_ratio * heavy_worker_ram_estimation))
limit_memory_soft = limit_memory_hard * 0.85  # Assuming soft limit is set to 85% of hard limit

# Calculate request and time limits
limit_request = 8192  # You can adjust this value based on your requirements
limit_time_cpu = 60
limit_time_real = 120

# Print the calculated values
print(f"limit_memory_hard: {limit_memory_hard} MB")
print(f"limit_memory_soft: {limit_memory_soft} MB")
print(f"limit_request: {limit_request}")
print(f"limit_time_cpu: {limit_time_cpu} seconds")
print(f"limit_time_real: {limit_time_real} seconds")