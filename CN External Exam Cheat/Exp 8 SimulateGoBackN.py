# Go-Back-N Sliding Window Protocol

total_frames = int(input("Enter total number of frames: "))
window_size = int(input("Enter window size: "))
lost_frame = int(input("Enter lost frame number (0 for no loss): "))

i = 1

while i <= total_frames:

    print("\nSending frames:")

    # Send frames within the window
    for j in range(i, min(i + window_size, total_frames + 1)):
        print("Frame", j, "sent")

    if lost_frame >= i and lost_frame < i + window_size:
        print("Frame", lost_frame, "lost!")
        print("Go-Back-N: Retransmitting from frame", lost_frame)

        # Retransmit lost frame and subsequent frames
        for j in range(lost_frame, min(i + window_size, total_frames + 1)):
            print("Frame", j, "retransmitted")
            print("ACK received for frame", j)

        i = min(i + window_size, total_frames + 1)

    else:
        for j in range(i, min(i + window_size, total_frames + 1)):
            print("ACK received for frame", j)

        i += window_size

print("\nAll frames transmitted successfully!")