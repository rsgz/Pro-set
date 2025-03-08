extern crate rdev;

use rdev::{simulate, Button, Event, EventType, Key};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 定义要点击的点
    let clicks = vec![(19, 199), (96, 409), (219, 408), (748, 333)];

    // 模拟鼠标点击
    for (x, y) in clicks {
        simulate(&Event::new(EventType::ButtonPress(Button::Left)))?;
        simulate(&Event::new(EventType::MouseMove { x, y }))?;
        simulate(&Event::new(EventType::ButtonRelease(Button::Left)))?;
    }

    // 模拟 Ctrl+A
    simulate(&Event::new(EventType::KeyPress(Key::LCtrl)))?;
    simulate(&Event::new(EventType::KeyPress(Key::A)))?;
    simulate(&Event::new(EventType::KeyRelease(Key::A)))?;
    simulate(&Event::new(EventType::KeyRelease(Key::LCtrl)))?;

    // 输入 "003"
    for c in "003".chars() {
        simulate(&Event::new(EventType::KeyPress(c)))?;
        simulate(&Event::new(EventType::KeyRelease(c)))?;
    }

    Ok(())
}
