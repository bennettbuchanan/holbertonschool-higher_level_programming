//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    @IBOutlet weak var labelCounter: UILabel!
    
    var timer = NSTimer()
    var counter = 0
    var taps_requested: Int = 0
    
    @IBAction func clickPlayButton(sender: AnyObject) {
        // Check to see if the text entered is an Int, intialize the game.
        
        let text: String = textfield_number.text!
        let int: Int? = Int(text)
        if int != nil && int > 0 {
            taps_requested = int!
            self.initGame()
            print("Let's do \(int!) taps")
        }
    }
    
    var taps_done: Int = 0
    
    @IBAction func clickCoinButton(sender: AnyObject) {
        // Increment taps_done, reset the game when exceeding taps_requested.
        
        print("Tap!")
        taps_done += 1
        label_taps.text = String(taps_done) + " Taps!"
        if taps_done >= taps_requested {
            self.resetGame()
        }
    }
    
    func countUp() {
        // Updates the counter.
        
        counter += 1
        updateText()
    }
    
    func updateText() {
        // Update the counter text.
        
        let text = String(counter)
        labelCounter.text = text
    }
    
    func initGame() {
        // Change the display properties of elements. Begin the counter.
        
        button_play.hidden = true
        image_tapper.hidden = true
        textfield_number.hidden = true
        label_taps.hidden = false
        labelCounter.hidden = false
        button_coin.hidden = false
        label_taps.text = "0" + " Taps!"
        
        timer = NSTimer.scheduledTimerWithTimeInterval(0.01, target: self, selector: #selector(ViewController.countUp), userInfo: nil, repeats: true)
        NSRunLoop.currentRunLoop().addTimer(timer, forMode: NSRunLoopCommonModes)
    }
    
    func resetGame() {
        // Reset values to 0, change the display properties of elements.
        
        taps_requested = 0
        taps_done = 0
        label_taps.hidden = true
        button_coin.hidden = true
        labelCounter.hidden = true
        image_tapper.hidden = false
        button_play.hidden = false
        textfield_number.hidden = false
        
        timer.invalidate()
        counter = 0
        updateText()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}

