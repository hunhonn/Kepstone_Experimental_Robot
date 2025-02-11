fn main() {
    rosrust::rosmsg_include!(std_msgs/String,sensor_msgs/Imu,roscpp_tutorials/TwoInts);
    // Initialize node
    rosrust::init("talker");

    // Create publisher
    let chatter_pub = rosrust::publish("chatter", 100).unwrap();

    let mut count = 0;

    // Create object that maintains 10Hz between sleep requests
    let rate = rosrust::rate(10.0);

    // Breaks when a shutdown signal is sent
    while rosrust::is_ok() {
        // Create string message
        let mut msg = rosrust_msg::std_msgs::String::default();
        msg.data = format!("hello world {}", count);

        // Send string message to topic via publisher
        chatter_pub.send(msg).unwrap();

        // Sleep to maintain 10Hz rate
        rate.sleep();

        count += 1;
    }
}
