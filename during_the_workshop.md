# Chessington

## The Brief

> We've started work on the Chessington app! The UX Team came up with a novel interface, and we've built the game engine and GUI. Problem is, Geoff is the only one who knows the rules of chess and he's gone for a really long lunch. We haven't been able to finish the job without him. That's where you come in.  
> Start with the simple pieces and we'll go from there. Management recently signed off a TDD approach so let's try that out. Work in pairs to keep that knowledge sharing up. Hopefully that'll reduce our dependence on Geoff in future…

Fork and clone this repo, then follow the instructions in [README.md](./README.md) to get the app and tests running.

## Part 1

When you're ready, run `git cherry-pick red-1`. You'll notice some new unit tests have appeared! Run the unit tests and see what's failed. Working in a pair, implement the minimum functionality required to pass the tests.

Repeat this for red-2 through red-5, switching driver each time.

### Tips

* This is TDD, with someone else providing the tests.
* You won't need to make changes to the chessington/ui package (although feel free to explore it).
* Avoid print statements! If you need to debug an error, use the VSCode debugger.
* Use VSCode live share to work with your pair.

## Part 2 (stretch)

You've programmed Pawn movement, now for the rest of the pieces. We don't have any unit tests for these so you'll need to write them first.

For each of the following pieces, write unit tests and functionality following TDD. Make sure you follow the Red-Green-Refactor cycle! For this part, use ping-pong pairing. That means the driver writes a unit test, then the navigator makes it pass. Switch roles after every test.

1. King
2. Knight
3. Bishop
4. Rook
5. Queen

Stick to basic movement and capture tests. Don't worry about any of the more complex rules (check, checkmate, castling etc.) just yet.

## Part 3 (stretch)

Chessington can now play chess! But the game never ends, and it's missing some of the more situational rules. If you have time, work through the list of rules below using ping-pong pairing:

1. En Passant
2. Castling
3. Pawn Promotion
4. Check and Check Mate
5. Stalemate

Remember, only write code to make test cases pass. If you're not sure what these rules are, ask your pair or check online!
