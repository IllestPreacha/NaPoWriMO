=begin

live_loop :home do 
 play :Cs2 ,attack: 0.2   ,release: 3 ,amp: 0.5 
 sleep 0.25 
 sleep 2 
 end 

=end


live_loop :home do
  with_fx :ixi_techno,amp: 10.6 do
    with_fx :krush, amp: 10.6 do
      use_bpm 21.2 + 100
      with_fx [:vowel,:krush,:ixi_techno].choose, amp: 10.6, mix: rrand(0.202,0.519),amp: 1.568 do
        #use_synth :prophet
        sample [:drum_bass_hard,:guit_e_fifths].choose, rate: 5.356, beat_stretch: 0.519,sustain: 7.810 ,release: 5.356, pitch: 22.936/12.477
        sleep [100/50,54/27,100/79].choose
      end
    end
  end
end

live_loop :home1 do
  with_fx [:whammy,:ixi_techno].choose, amp: 5.356 do
    with_fx :distortion, amp: 5.356 do
      use_bpm 79 + 54
      with_fx [:vowel,:ixi_techno,:flanger].choose, amp: 5.356, mix: rrand(0.202,0.519),amp: 1.568 do
        #use_synth :prophet
        sample :loop_mehackit1, rate: 1.913, beat_stretch: 0.519,sustain: 7.810 ,release: 5.356, pitch: 10.6
        sleep [100/50,54/27,100/79].choose
      end
    end
  end
end


#=begin
live_loop :vyber do
  with_fx [:whammy,:ixi_techno,:flanger].tick, mix: 0.7 do
    play [chord(:Cs3,[:minor7,:major7].tick)].choose, sustain: dice(2)
    play [chord([:Fs4,:Bs3,:Ds2].tick,:major7)].choose, attack: 1.0
    sleep [0.25,0.5,1,2].choose
  end
end
#=end
