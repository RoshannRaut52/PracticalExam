# Selective Repeat Sliding Window Protocol

total_frames = int(input("Enter total number of frames: "))
window_size = int(input("Enter window size: "))
lost_frame = int(input("Enter lost frame number (0 for no loss): "))

i = 1

while i <= total_frames:

    print("\nSending frames:")

    # Send frames within the window
    for j in range(i, min(i + window_size, total_frames + 1)):
        print("Frame", j, "sent")

    # Check whether a frame is lost
    if lost_frame >= i and lost_frame < i + window_size:
        print("\nFrame", lost_frame, "lost!")

        # Acknowledge other frames
        for j in range(i, min(i + window_size, total_frames + 1)):
            if j != lost_frame:
                print("ACK received for frame", j)

        # Retransmit only the lost frame
        print("\nRetransmitting only frame", lost_frame)
        print("Frame", lost_frame, "retransmitted")
        print("ACK received for frame", lost_frame)

    else:
        for j in range(i, min(i + window_size, total_frames + 1)):
            print("ACK received for frame", j)

    i += window_size

print("\nAll frames transmitted successfully!")