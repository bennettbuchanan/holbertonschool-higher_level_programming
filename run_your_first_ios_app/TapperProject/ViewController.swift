//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit
import Social

class ViewController: UIViewController {
    // ViewController class for Tapper game.
    
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    @IBOutlet weak var labelCounter: UILabel!
    @IBOutlet weak var highScore: UILabel!
    
    let best_taps_score = "best_taps_score.txt"
    var timer = NSTimer()
    var counter = 0
    var taps_requested: Int = 0
    
    override func viewDidAppear(animated: Bool) {
        highScore.text = getHighScore()
    }
    
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
        fileSave(counter)
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
    
    @IBAction func twitterButtonPushed(sender: AnyObject) {
        // Opens an option to share on Twitter.
        if SLComposeViewController.isAvailableForServiceType(SLServiceTypeTwitter) {
            
            let tweetShare:SLComposeViewController = SLComposeViewController(forServiceType: SLServiceTypeTwitter)
            
            self.presentViewController(tweetShare, animated: true, completion: nil)
            
        } else {
            
            let alert = UIAlertController(title: "Accounts", message: "Please login to a Twitter account to tweet.", preferredStyle: UIAlertControllerStyle.Alert)
            
            alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
            
            self.presentViewController(alert, animated: true, completion: nil)
        }
    }
    
    func fileSave (time: Int) {
        // Take the time the user reached and write it to a file.
        let gameTime = String(time)
        
        if let dir = NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory.DocumentDirectory, NSSearchPathDomainMask.AllDomainsMask, true).first {
            let path = NSURL(fileURLWithPath: dir).URLByAppendingPathComponent(best_taps_score)
            
            // Write
            do {
                try gameTime.writeToURL(path, atomically: false, encoding: NSUTF8StringEncoding)
            }
            catch {/* error handling here */}
            
            
            do {
                let gameTime = try NSString(contentsOfURL: path, encoding: NSUTF8StringEncoding)
                print(gameTime)
                highScore.text = "Be fast: " + (gameTime as String)
            }
            catch {/* error handling here */}
        }
    }
    
    func getHighScore() -> String {
        // Return the high score stored in the file for intial display.
        if let dir = NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory.DocumentDirectory, NSSearchPathDomainMask.AllDomainsMask, true).first {
            let path = NSURL(fileURLWithPath: dir).URLByAppendingPathComponent(best_taps_score)
            
            do {
                let gameTime = try NSString(contentsOfURL: path, encoding: NSUTF8StringEncoding)
                return "Be fast: " + (gameTime as String)
            }
            catch {/* error handling here */}
        }
        return "Be fast: "
    }
}

